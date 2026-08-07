---
layout: post
title: "Offline Evaluation Frameworks for AI Agents"
date: 2026-08-07 00:00:00 +0000
author: "Andrei Radulescu-Banu"
image: /assets/images/ai_agent_offline_evaluation.png
categories: [ai, engineering]
description: "Offline evaluation for DocRouter’s Document Agent (Smart Agent Kit), plus the same pattern applied to medical insurance claim evaluation."
---

Classic software needs unit tests. Prompt-based and agent systems need them more—and they behave differently. Language models are __stochastic__: a one-line prompt tweak ripples across many paths. Fix case ten and you silently break cases one and two. So every meaningful change forces a __wide retest__ across inputs and configurations—not a single happy-path check. That is what [offline evaluation infrastructure](/ai/programming/tutorials/how-to-train-your-ai-agent/) is for: you cannot improve what you do not measure.

## Offline vs online evaluation

This post focuses on __offline evaluation__—but __online evaluation__ matters just as much. __Offline evaluation__ uses controlled, replayable datasets to measure behavior and regressions—labeled expectations (facts, references, assertions) and suite re-runs before you ship a change. __Online evaluation__ measures behavior on real production traffic using telemetry, automated checks, product outcomes, and explicit user feedback. Typical online setups export agent tool calls and traces with __OpenTelemetry__, and let users leave thumbs-up / thumbs-down or short textual feedback that engineering and product teams use for triage.

Our product [SigAgent.AI](https://sigagent.ai) implements online evaluation for Claude agents. We will cover online evaluation in a later post.

## Offline evaluation

We built an offline evaluation framework—the __Smart Agent Kit__—for DocRouter’s __Document Agent__, the coding agent that configures schemas, prompts, and tags through a multi-tool agent loop. The same loop applies when you evaluate other agents. Figure 3 maps that loop onto a __medical insurance__ coverage-assessment agent:

1. Define a __dataset__ of representative cases (tagged for selective reruns)  
2. Capture what “good” looks like carefully: __ground-truth facts__, __reference solutions__, and __assertions / invariants__  
3. Run the agent __offline__, recording __tool-call traces__ and __cost__  
4. Score with __deterministic graders__ first, then one or more __LLM judge rubrics__ where nuance is needed  
5. Re-run the full suite—or a __tagged slice__—when something changes, so offline eval stays affordable  

This post walks through that loop in the Smart Agent Kit, then applies the same architecture to medical claims.

<img src="/assets/images/ai_agent_offline_evaluation.png" alt="Offline evaluation architecture for AI agents" style="width: 80%; height: auto;">

<p style="text-align: center; font-size: 0.875rem; color: #6b7280;"><strong>Figure 1:</strong> Offline evaluation: dataset → agent run → deterministic graders → LLM judge rubric(s) → scored results.</p>

## One pattern, two domains

The first half is the __Smart Agent Kit__ (Document Agent)—what we built. The second is __medical insurance__ claim evaluation (Figure 3). Figures 2 and 3 share one architecture vocabulary (agent → dataset → tasks/tags → test run → trials → per-task evaluation → aggregates); only the agent, task shape, and graders change. Figure 3 is a design—not a product we have shipped.

### Smart Agent Kit — evaluating DocRouter’s Document Agent

DocRouter includes a [__Document Agent__](/docs/document-agent/): a coding agent that sets up extraction in plain language. It runs an __agent loop__ with many tools—create and validate schemas, write prompts, attach tags, run extraction, and more—so configuration is tool-calling work, not a single model response. That raises a hard question: __how do you measure whether the Document Agent is accurate and effective?__

You cannot judge it from chat fluency alone. The __Smart Agent Kit__ (`smaht-agent-kit`) is the offline evaluation framework for that Document Agent. Figure 2 is the model; the sections below follow it.

<div data-excalidraw="/assets/excalidraw/offline_evaluation_smart_agent_kit.excalidraw" class="excalidraw-container">
  <div class="loading-placeholder">Loading diagram...</div>
</div>
<div style="text-align: center; margin-top: 1rem;">
  <a href="/excalidraw-edit?file=/assets/excalidraw/offline_evaluation_smart_agent_kit.excalidraw" target="_blank" style="color: #2563eb; text-decoration: none; font-weight: 500;">
    📝 Edit in Excalidraw
  </a>
</div>
<p style="text-align: center; margin-top: 0.5rem; font-size: 0.875rem; color: #6b7280;"><strong>Figure 2:</strong> Smart Agent Kit — agent under test → dataset → tasks/tags → test run (selected slice) → 1..k trials (result · trace · cost) → per-task evaluation (graders · rubrics · pass@k / pass^k) ← facts / reference / assertions → test-run / dataset aggregates.</p>

__1. Agent under test.__ The subject is DocRouter’s __Document Agent__: agent loop, many MCP tools, schemas / prompts / tags, validate, extract. Offline evaluation __gets expensive__—each trial is a multi-turn agent loop plus grader passes—so the kit __tracks cost__ (tokens / API cost and latency) per trial, rolled up per task and per test run.

__2. Dataset.__ The kit supports __multiple datasets__ of configuration work (different suites you select for a run).

__3. Tasks / cases + tags.__ Each dataset is a collection of __tasks__—configuration jobs for the coding agent (create a CV schema and prompt, set up an invoice schema, validate and fix an invalid schema, and so on). Each task is __tagged__ (`schema`, `validation`, `invoice`, `regression`, …) so you filter before a rerun.

__4. Test run — selected dataset slice.__ A __test run__ executes a suite over a dataset slice. Choose a __full suite__ (baseline / release) or a __tagged slice__ (e.g. after a schema-tool fix, run `schema` + `validation` only). Same dataset; \(k\) and tag filters control cost. Historical test runs live in timestamped folders (results, evals, traces, cost).

__5. 1..k trial runs per task.__ For each selected task the test run executes __1..k trials__. Each trial records a __result__ (produced artifacts: schema JSON, prompt JSON, tags, extraction setup), a __tool-call trace__ (name, arguments, result, order, timing), and __cost / latency__ for that trial. Traces are the __primary diagnostic signal__—not a brittle expected script. Agents find different valid paths—and different valid artifacts—to satisfy the same task; requiring one sequence or one golden schema makes the eval brittle.

__6. Per-task evaluation across trials.__ Graders score each trial; those scores aggregate into a __per-task evaluation__—success rate, mean rubric scores, __pass@k__ / __pass^k__—not a single lucky or unlucky sample. Scoring is fed by __ground-truth facts__, a __reference solution__, and __assertions / invariants__ (see below)—not byte-for-byte identity with whoever wrote the example:

1. __Deterministic graders__ — JSON parses; schema validator passes; required fields exist; expected tag exists; required tool was invoked (when that is an invariant); artifact exists; extraction executes; assertion checks and, only where appropriate, structural diffs against a reference.  
2. __LLM judge rubrics__ — semantic judgment against the task and reference. Often more than one rubric: e.g. concept coverage, prompt quality, intent match, completeness—without requiring the agent’s schema to look like ours.  
3. __Per-task summaries__ — success rate / pass@k / pass^k (plus cost) across the task’s trials.

Code-based graders are cheaper, reproducible, and objective; LLM rubrics cover what code-based grading cannot. We grade the tool-call path strictly only when the path itself is the requirement.

__7. Test-run / dataset aggregates.__ Task-level results roll up into suite metrics: __segment scores__ (by tag / slice), __total cost / latency__, and __historical comparison__ across timestamped runs. The debug path is: failing task score → open a trial’s tool timeline → fix the agent or tools → retag and rerun the slice.

The kit evaluates a __tool-using coding agent__, not PDF extraction accuracy.

### Insurance claim evaluation

Figure 3 shows offline evaluation for a medical insurance __coverage assessment__ agent. It is a design—not a product we have shipped. Like the Document Agent, the __Benefits Examiner__ is assumed to be a __tool-using__ agent—policy lookup, claim detail, knowledge-base retrieval, and related tools—so the same offline loop (tool traces, trials, graders) applies.

Figure 3 uses the same seven steps as Figure 2. The __agent under test__ is the Benefits Examiner (and, later, other agents). __Datasets__ are suites of claim __tasks / cases__ with tags; a __test run__ selects a dataset slice (full suite or tagged). Each selected task runs __1..k trials__, recording __result__ (structured assessment), __trace__, and __cost / latency__. __Per-task evaluation__ grades those trials with deterministic graders and LLM rubrics against labeled expectations—claim/policy __facts__, expert-labeled __decisions__, a __reference__ assessment, and __assertions__—then summarizes with success rate / pass@k / pass^k. __Test-run / dataset aggregates__ add segment scores, total cost / latency, and historical comparison. Operators promote a strong agent result into the labeled set after domain-expert review.

<div data-excalidraw="/assets/excalidraw/offline_evaluation_medical_claims.excalidraw" class="excalidraw-container">
  <div class="loading-placeholder">Loading diagram...</div>
</div>
<div style="text-align: center; margin-top: 1rem;">
  <a href="/excalidraw-edit?file=/assets/excalidraw/offline_evaluation_medical_claims.excalidraw" target="_blank" style="color: #2563eb; text-decoration: none; font-weight: 500;">
    📝 Edit in Excalidraw
  </a>
</div>
<p style="text-align: center; margin-top: 0.5rem; font-size: 0.875rem; color: #6b7280;"><strong>Figure 3:</strong> Medical insurance (design)—same architecture as Figure 2: agent under test → dataset → tasks/tags → test run → 1..k trials (result · trace · cost) → per-task evaluation ← facts / reference / assertions → test-run / dataset aggregates; human-reviewed promotion into the labeled set.</p>

<style>
.excalidraw-container {
  width: 100%;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  background: white;
  display: block;
  margin: 2rem 0;
  min-height: 400px;
}

.excalidraw-container svg {
  width: 100%;
  height: auto;
  display: block;
  margin: 0;
}

.loading-placeholder {
  padding: 2rem;
  text-align: center;
  color: #666;
}
</style>

<script type="module" src="/assets/js/excalidraw/render-excalidraw.js"></script>

Both answer the same operational question: __when we change the agent, did quality go up or down—and on which kinds of work?__

## Datasets: the unit of offline work

A dataset is a versioned collection of cases the agent must handle without a human in the loop.

For the Smart Agent Kit, that means the configuration __tasks__ in Figure 2. For medical insurance evaluation (Figure 3), datasets are suites keyed by agent: tasks include claim numbers, date of service, encounter types, categories, and tags. A __test run__ is always “this agent × this dataset × these filters”—and for each selected task, __1..k trial runs__—not an ad-hoc list of IDs in a notebook.

Datasets make evaluation __reproducible__. Re-run the same suite after a prompt change, a model swap, or a tool fix, and compare scores (and cost) across timestamped result folders.

## What “correct” means: facts, reference, assertions

Calling everything “ground truth” is a subtle trap—especially for a coding or configuration agent.

The same task often admits __multiple correct schemas or prompts__. If you write:

> expected schema = ground truth

it quietly becomes:

> the schema must look like the one we happened to write.

That penalizes valid alternatives and fights the same creativity you want from a tool-using agent (different valid tool paths, different valid artifacts). Distinguish three things:

| | Role | Example (Document Agent) |
|--|------|--------------------------|
| __Ground-truth facts__ | Things that objectively must be true | Required field names the task asked for; tag must exist; JSON must validate; extraction must run |
| __Reference solution__ | One known-good example | A schema/prompt pair that works for the task—useful for humans and for LLM rubrics, not the sole passing shape |
| __Assertions / invariants__ | Conditions __any__ valid solution must satisfy | “Includes patient name and dates”; “schema validates”; “prompt mentions invoice totals”; “`validate_schema` ran if the task requires it” |

A __reference schema is not necessarily the only correct schema__. The evaluator combines known-good artifacts with objective assertions and semantic grading so alternative valid solutions are not penalized. Exact structural diffs against the reference are a tool of last resort—useful when the task truly has one canonical shape, harmful when it does not.

For the Document Agent (Figure 2), much of the outcome check is therefore __deterministic assertions__ (parse, validate, required fields, tags, artifacts, extraction executes). We use LLM judge rubric(s) where semantics matter—comparing intent and coverage to the task and the reference—while keeping __outcome grading__ dominant unless a particular tool path is itself a requirement. The tool-call trace sits beside the files so you see __how__ the agent got there when something fails—without treating one expected sequence (or one expected schema) as the only valid path.

For medical insurance evaluation (Figure 3), labeled expectations share one structured shape with the agent result:

- __Benefit decisions__ — service/benefit line, disposition (payable / deny / pend / partial), plan citation, network, cost share, medical necessity, confidence  
- __Open facts__ — clinical, coding, auth, eligibility, COB—information still needed before a firm determination  
- __Examiner summary__ — narrative write-up for the claim  
- __Headline determination__ — payable / deny / pend / partial  

The three-way split still applies, with one medical refinement: objective claim and policy attributes (DOS, codes, eligibility, network status, and so on) may be __ground-truth facts__; headline and benefit dispositions (payable / deny / pend / partial) are __expert-labeled decisions__, not facts in the same sense; an examiner write-up is a __reference solution__; and requirements such as “must cite the plan,” “must flag this open fact,” or “required benefit lines present” are __assertions__. Load a labeled expectation next to an agent result, edit it, and promote a strong agent result into the labeled set __after domain-expert review__—not because an LLM rubric scored it highly.

That last step matters in practice. Offline evaluation is not only for scoring; it is how you __grow__ the labeled set—without freezing creativity into a single golden file, and without letting agent output quietly become tomorrow’s “ground truth” because a model approved itself.

## Parallel evaluation: throughput without serial waiting

Agent runs are often the expensive part of a suite—minutes per claim or per multi-tool Document Agent session. Run task trials in parallel (configurable worker count), so a ten-claim suite does not take ten times one claim’s wall clock. Each worker collects the agent result and tool events; the runner still preserves task order in the saved output, still grades each trial, and still builds __per-task__ then __test-run__ aggregates—parallelism only changes wall-clock scheduling, not the Dataset → Task → Trial → per-task aggregate → test-run aggregate hierarchy below.

Parallelism keeps offline eval usable as datasets grow. You still pay for every model call, but you get answers in a sitting instead of overnight—and you schedule full-suite regressions without blocking day-to-day development.

## Repeatability: dataset → task → trials → per-task evaluation → test-run aggregates

The opening point about stochasticity leaves a methodological hole if every diagram is read as __one task → one agent execution → one score__. If you change a prompt and task 17 drops from 85 to 72 on a rubric, was the agent worse—or was that trial-to-trial noise?

Keep the hierarchy distinct—consistent with Anthropic’s usage where a __task__ is one test case and a __trial__ is one attempt at that task:

| Term | Meaning |
|------|---------|
| __Dataset__ | Versioned collection of __tasks__ |
| __Task__ | One case in the dataset (a configuration job, or one claim)—one test case |
| __Trial__ | One execution of the agent on that task |
| __Test run__ | One suite execution: select tasks/tags, then for each selected task run __1..k trials__ |
| __Per-task evaluation__ | Aggregate of that task’s graded trials in the test run (success rate, mean scores, pass@k / pass^k) |
| __Test-run / dataset aggregate__ | Roll-up of per-task evaluations (plus cost) for the suite |

__Evaluation happens at two levels.__ Each trial is graded individually, then those scores are aggregated into a __per-task evaluation__ across the task’s trials. Finally, task-level results are aggregated across the __test run__. A single trial is a sample, not the agent. Two common summaries of those trials: __pass@k__ asks whether at least one of \(k\) trials succeeds; __pass^k__ asks whether all \(k\) trials succeed. The former measures capability with multiple attempts; the latter is useful for reliability—the same capability-versus-consistency distinction Anthropic draws. Ten trials on every task fights the cost-control story. A practical split:

- __Fast development test runs__ — one trial per task, tagged slices, cheap feedback while iterating.  
- __Important regressions / release baselines__ — multiple trials on critical or known-unstable tasks; report reliability across trials, not a lone score.  
- __Unstable tasks__ — tag them and spend budget where variance is high; keep one-shot trials on boring, stable work.

That closes the loop with stochasticity: offline eval measures reliability under sampling, not a single lucky or unlucky path.

Reproducibility also means versioning the system under evaluation and the evaluator itself. Each test run should record the dataset version, agent/code version, model and configuration, tool definitions, grader/rubric versions, selected tasks or tags, and trial count \(k\)—and model parameters where relevant. Otherwise an old score may be impossible to reproduce—or even interpret—after the agent or judges change. Timestamped result folders are useful history; versioned run config is what makes “87 on August 1, 92 on August 7” a comparison you can trust.

## Tagging for segmentation

Not every change needs every case. Tags turn a flat dataset into slices you reason about—and, as Figure 2 stresses for the Smart Agent Kit, into a __cost control__ lever when offline evaluation is expensive.

Tag medical claim cases by complexity and pattern—for example `simple`, `complex`, `outpatient`, `inpatient`, `home_health`, `dme`, `ambulance`, `lab`, `imaging`, `rx`, `behavioral`, `in_network`, `out_of_network`. Operators select a tag subset before running.

Document Agent tasks use the same idea (`schema`, `validation`, `invoice`, `regression`). Because the agent tracks cost per trial and per test run, you see the bill for a full suite versus a tagged slice—and choose the cheaper path when only part of the agent changed.

Segmentation pays off in three ways:

- __Diagnosis__ — if scores drop only on `complex` + `behavioral` (or only on `dme` tasks), you know where to look.  
- __Efficiency__ — after a narrowly scoped change, re-run the affected tags instead of the whole suite.  
- __Cost__ — fewer agent invocations and fewer rubric calls when you do not need a full regression.

## Grading: deterministic first, then LLM judge rubric(s)

“LLM-as-judge” is a useful shorthand—but it is not one monolithic scorer. The Smart Agent Kit—and the medical design in Figure 3—run __deterministic graders__ first, then zero or more __LLM judge rubrics__: each rubric is a separate model call (or a structured multi-score prompt) that receives the agent output plus reference artifacts and asserted facts when available, and returns scores with written reasoning. Rubrics differ by dimension (accuracy, completeness, intent, domain-specific checks) and by domain (Document Agent vs medical claim); add or retire rubrics without collapsing everything into a single “quality” number.

__Deterministic checks → LLM judge rubric(s) → per-task aggregate (across trials) → test-run / dataset aggregates__

For the Document Agent, a surprising amount is objective __assertion__ work: JSON parses; schema validator passes; required fields exist; expected tag exists; a required tool was invoked; extraction executes; the artifact exists. Structural comparison against a __reference__ schema is optional and easy to overuse. LLM rubrics cover what needs semantic judgment against the task (and the reference as a guide)—for example concept coverage, prompt appropriateness, intent match, completeness—even when the JSON differs from the known-good example.

Code-based graders are cheaper, reproducible, and objective. Model rubrics are valuable where nuance is necessary.

| Grader | Examples |
|--------|----------|
| __Deterministic__ | Schema validity, required fields, artifact presence, required tools, assertion checks; structural diffs vs reference only when the shape is truly canonical |
| __LLM judge rubric(s)__ | Separate or combined scores for semantic accuracy, completeness, intent match vs task + reference (not “must match our file”); for medical claims, rubrics for benefit reasoning, open facts, narrative quality |
| __Human sampling__ | Calibration and disputed cases |

Those layers produce a score per trial; the runner then builds a __per-task evaluation__ across that task’s trials, and finally __test-run / dataset aggregates__ (overall success rate and __total cost__). Re-run deterministic checks and selected rubrics after editing labels without necessarily re-running the agent. Domain-shaped checks beat vague “quality” scores: an agent looks fluent while missing a required field, skipping a required invariant, or contradicting a __ground-truth fact__.

### How accurate are the LLM judges?

1. __A judge model does not have to be the agent model.__ Choose each judge independently. Validate a smaller or cheaper judge against human judgments before you trust it.  
2. __Judging is easier than doing.__ Comparing a result to facts, assertions, and a reference is a narrower task than generating the result in the first place. Still: do not treat any single rubric score as automatically authoritative.  
3. __Calibrate rubrics against humans.__ Periodically have domain experts score a sample, compare those judgments with each LLM rubric, and adjust the rubric prompt—or split/merge rubrics—when they diverge.

Treat each LLM judge rubric as a __scalable grader__, not as ground truth—and treat a reference artifact as a known-good example, not as the only allowed answer. The same rule applies when growing labels: high rubric scores __nominate__ a run for the labeled set; only __human / domain-expert review__ promotes it.

## Tracing tool calls

Scores tell you __whether__ something failed. Traces tell you __how__. For the Smart Agent Kit (Figure 2), every __trial__ stores tool name, arguments, result, order, and timing so you open a failing trial and inspect the timeline. Use traces to debug—wrong tool, skipped step, failed create—not as the default pass/fail script. Prefer outcome grading; enforce path constraints only when the path is the requirement. The debug loop is: failing task score → open a trial’s tool timeline → fix the agent or tools → retag and rerun the slice.

Store medical traces the same way—alongside results and evaluations (tool name, inputs, results)—so you replay policy lookup, claim detail, knowledge base retrieval, and related tools.

## Re-run the suite—or only what you need

Offline evaluation only works if re-running is cheap enough that people actually do it. Figure 2’s cost-control panel is the Smart Agent Kit version of that rule: full suite when you need a baseline; tagged slices when the change is narrow.

The same capabilities apply to medical evaluation:

- __Full dataset test runs__ — baseline or release regression across every task (expensive; visible in cost totals).  
- __Scoped test runs__ — by tag set or by task IDs; still __1..k trial runs__ per selected task.  
- __Single-task re-runs__ — re-execute one claim or one Document Agent task after a fix (again with chosen \(k\)).  
- __Judge-only re-evaluation__ — re-score with deterministic graders and/or selected LLM rubrics against updated facts, assertions, or reference artifacts without paying for another agent pass.

Use the full suite when you change something global (model, shared tools, core system prompt). Use tags when the change is local. Use judge-only passes when you are refining labels or rubrics, not agent behavior.

Results live in timestamped folders—agent outputs, evaluations, tool traces, and cost totals—so you keep a history of quality and spend, not a single overwritten spreadsheet.

## Closing

Offline evaluation frameworks turn agent development into engineering: a dataset of real cases; success defined by facts, assertions, and reference solutions (not a single golden file where alternatives exist); deterministic graders before model graders; tool-call traces for debugging; cost tracking; enough trials to separate signal from stochastic noise; and the ability to re-run everything—or only the tagged slice that matters.

We built the Smart Agent Kit for DocRouter’s Document Agent. Figure 2 centers that story on outcome grading that tolerates valid alternatives, traces as diagnostics, and cost-aware tag-filtered reruns; Figure 3 applies the same pattern to medical insurance claims. The domains differ; the discipline does not. If you are building custom agents, start labeled cases early, keep facts distinct from reference artifacts, score every meaningful change, and treat evaluation as part of the product—not a one-off demo script.

## Further reading

- [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) — Anthropic Engineering (task vs trial, pass@k / pass^k, and related agent-eval practice)
