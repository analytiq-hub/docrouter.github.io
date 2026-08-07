---
layout: post
title: "Offline Evaluation Frameworks for AI Agents"
date: 2026-08-07 00:00:00 +0000
author: "Andrei Radulescu-Banu"
image: /assets/images/ai_agent_offline_evaluation.png
categories: [ai, engineering]
description: "Offline evaluation for DocRouter’s Document Agent (Smart Agent Kit), plus the same pattern applied to medical insurance claim evaluation."
---

Classic software needs unit tests. Prompt-based and agent systems need them even more—and they behave differently.

Language models are **stochastic**: a one-line prompt change can ripple across many paths. Fix case ten and you may silently break cases one and two. So meaningful changes require a **wide retest** across representative inputs and configurations, not a single happy-path check.

That is what [offline evaluation infrastructure](/ai/programming/tutorials/how-to-train-your-ai-agent/) is for: you cannot improve what you do not measure.

## Offline vs online evaluation

**Offline evaluation** uses controlled, replayable datasets to measure behavior and regressions. You define representative cases and labeled expectations, run the agent, score the results, and repeat the suite after changes.

**Online evaluation** measures behavior on real production traffic using telemetry, automated checks, product outcomes, and explicit user feedback. Typical setups capture tool calls and traces with **OpenTelemetry** and collect signals such as thumbs-up / thumbs-down or textual feedback for engineering and product teams.

Our product [SigAgent.AI](https://sigagent.ai) implements online evaluation for Claude agents. We will cover online evaluation in a later post.

This post focuses on offline evaluation.

## The offline evaluation loop

We built the **Smart Agent Kit** for DocRouter’s **Document Agent**, a coding agent that configures schemas, prompts, and tags through a multi-tool agent loop.

The same basic pattern applies to many other agents:

1. Define a **dataset** of representative tasks, tagged for segmentation and selective reruns.
2. Define what “good” means using **facts**, **reference solutions**, and **assertions / invariants**.
3. Run the agent offline, usually with **1..k trials per task**, recording results, traces, cost, and latency.
4. Score each trial with **deterministic graders first**, followed by **LLM judge rubrics** where semantic judgment is needed.
5. Aggregate results per task and across the test run, then rerun the full suite—or only the affected slice—after changes.

<img src="/assets/images/ai_agent_offline_evaluation.png" alt="Offline evaluation architecture for AI agents" style="width: 80%; height: auto;">

<p style="text-align: center; font-size: 0.875rem; color: #6b7280;"><strong>Figure 1:</strong> Offline evaluation: dataset → agent run → deterministic graders → LLM judge rubric(s) → scored results.</p>

## One pattern, two domains

Figures 2 and 3 use the same architecture:

**agent → dataset → tasks/tags → test run → trials → per-task evaluation → test-run aggregates**

Figure 2 shows the **Smart Agent Kit**, which we built for DocRouter’s Document Agent. Figure 3 applies the same pattern to a **medical insurance coverage-assessment agent**. The medical example is a design, not a product we have shipped.

### Smart Agent Kit — evaluating DocRouter’s Document Agent

DocRouter’s [**Document Agent**](/docs/document-agent/) sets up document extraction in plain language. It uses many tools: creating and validating schemas, writing prompts, attaching tags, running extraction, and more.

Because this is a tool-using coding agent, chat fluency is not enough to tell us whether it worked.

The **Smart Agent Kit** (`smaht-agent-kit`) evaluates the actual outcome.

<div data-excalidraw="/assets/excalidraw/offline_evaluation_smart_agent_kit.excalidraw" class="excalidraw-container">
  <div class="loading-placeholder">Loading diagram...</div>
</div>

<div style="text-align: center; margin-top: 1rem;">
  <a href="/excalidraw-edit?file=/assets/excalidraw/offline_evaluation_smart_agent_kit.excalidraw" target="_blank" style="color: #2563eb; text-decoration: none; font-weight: 500;">
    📝 Edit in Excalidraw
  </a>
</div>

<p style="text-align: center; margin-top: 0.5rem; font-size: 0.875rem; color: #6b7280;"><strong>Figure 2:</strong> Smart Agent Kit — agent under test → dataset → tasks/tags → test run → 1..k trials → per-task evaluation → test-run / dataset aggregates.</p>

The important pieces are:

* A **dataset** contains configuration tasks such as creating an invoice schema, building a CV extraction prompt, or repairing an invalid schema.
* Tasks carry **tags** such as `schema`, `validation`, `invoice`, and `regression`, allowing selective reruns.
* A **test run** selects a full dataset or a tagged slice.
* Each selected task runs **1..k trials**.
* Every trial records the resulting artifacts, the tool-call trace, cost, and latency.
* Deterministic graders and LLM rubrics score each trial.
* Trial scores aggregate into a **per-task evaluation**, then into test-run and dataset metrics.

Tool traces are primarily a **diagnostic signal**. Agents can take different valid paths and produce different valid artifacts. Requiring one exact tool sequence—or one golden schema—would make the evaluation unnecessarily brittle.

The kit evaluates the **tool-using coding agent**, not PDF extraction accuracy itself.

## What does “correct” mean?

Calling everything “ground truth” is a subtle trap, especially for coding and configuration agents.

A task may admit several correct schemas or prompts. If we say:

> expected schema = ground truth

we can accidentally turn that into:

> the schema must look like the one we happened to write.

Instead, separate three concepts:

|                             | Role                                            | Example                                               |
| --------------------------- | ----------------------------------------------- | ----------------------------------------------------- |
| **Ground-truth facts**      | Things that objectively must be true            | Required field names, valid JSON, expected tag        |
| **Reference solution**      | One known-good example                          | A schema/prompt pair known to work                    |
| **Assertions / invariants** | Conditions any acceptable solution must satisfy | “Includes patient name and dates”; “schema validates” |

A **reference solution is not necessarily the only correct solution**.

For the Document Agent, much of the evaluation can therefore be deterministic: JSON parses, schema validation passes, required fields and tags exist, extraction executes, and required invariants hold.

LLM judges are useful where semantics matter—for example, whether a prompt captures the requested intent or a schema adequately covers a concept.

The default should be to grade the **outcome**, not require one particular path to that outcome.

## The same pattern for medical insurance

Figure 3 applies the same architecture to a medical insurance **Benefits Examiner** agent. Assume the agent uses tools for policy lookup, claim details, knowledge-base retrieval, and related tasks.

<div data-excalidraw="/assets/excalidraw/offline_evaluation_medical_claims.excalidraw" class="excalidraw-container">
  <div class="loading-placeholder">Loading diagram...</div>
</div>

<div style="text-align: center; margin-top: 1rem;">
  <a href="/excalidraw-edit?file=/assets/excalidraw/offline_evaluation_medical_claims.excalidraw" target="_blank" style="color: #2563eb; text-decoration: none; font-weight: 500;">
    📝 Edit in Excalidraw
  </a>
</div>

<p style="text-align: center; margin-top: 0.5rem; font-size: 0.875rem; color: #6b7280;"><strong>Figure 3:</strong> Medical insurance evaluation — the same dataset → task → trial → evaluation pattern applied to structured coverage assessments.</p>

A trial might produce:

* **Benefit decisions** — service line, payable / deny / pend / partial, plan citation, network status, cost share, medical necessity
* **Open facts** — missing clinical, coding, authorization, eligibility, or COB information
* **Examiner summary** — narrative explanation
* **Headline determination** — payable / deny / pend / partial

Here the labeling distinction matters even more.

Objective claim and policy attributes—dates, codes, eligibility, network status—may be **ground-truth facts**. Benefit dispositions are better treated as **expert-labeled decisions**. An examiner write-up can serve as a **reference solution**, while requirements such as “must cite the plan” or “must surface this open fact” are **assertions**.

A strong agent result can be promoted into the labeled set, but only **after domain-expert review**. A high LLM-judge score should nominate a result for review, not silently turn it into tomorrow’s ground truth.

This is an important secondary role for offline evaluation: it helps you **grow the labeled dataset** safely over time.

## Trials and stochasticity

A single agent run is a sample, not the agent.

Keep four terms distinct:

| Term         | Meaning                                      |
| ------------ | -------------------------------------------- |
| **Dataset**  | Versioned collection of tasks                |
| **Task**     | One test case                                |
| **Trial**    | One execution of the agent on that task      |
| **Test run** | One suite execution over selected tasks/tags |

Each trial is graded individually. Trial scores then aggregate into a **per-task evaluation**, and task-level results roll up into the overall test run.

Multiple trials matter because agents are stochastic. If task 17 scores 85 today and 72 after a prompt change, one run cannot tell you whether the agent really became worse.

Two useful summaries are:

* **pass@k** — did at least one of (k) trials succeed?
* **pass^k** — did all (k) trials succeed?

The first measures capability with multiple attempts. The second is useful for reliability.

But running ten trials on every task quickly becomes expensive. In practice:

* use **one trial** for fast development feedback,
* use **multiple trials** for release baselines and critical tasks,
* spend extra trials on tasks known to have high variance.

## Grading: deterministic first, LLM judges second

“LLM-as-judge” should not mean handing the entire evaluation problem to another model.

Use **deterministic checks** wherever possible:

* schema validation
* required fields
* artifact presence
* expected tags
* required tool use when genuinely required
* assertion checks
* structural comparison only when the output really has one canonical shape

Then use one or more **LLM judge rubrics** for semantic questions such as completeness, intent match, prompt quality, or domain reasoning.

The pipeline becomes:

**Deterministic checks → LLM rubric(s) → per-task aggregate → test-run aggregate**

LLM judges should themselves be evaluated. A judge model does not have to be the same model as the agent. Periodically compare judge scores against human or domain-expert judgments and adjust the rubric when they diverge.

Treat LLM judges as **scalable graders**, not ground truth.

## Make evaluation cheap enough to use

Offline evaluation only works if engineers actually rerun it.

Three features make that practical.

First, **tags** let you segment the dataset. After a narrow schema-tool change, run `schema` and `validation`; after a model or system-prompt change, run the full suite. Tags also show where regressions concentrate—for example, only on `complex` claims or `behavioral` cases.

Second, track **cost and latency** as evaluation metrics. An agent that becomes slightly more accurate but three times slower or more expensive may still be a regression.

Third, keep **tool traces** with every trial. Scores tell you whether something failed; traces tell you how. A useful debugging loop is:

**failing task → inspect trial trace → fix agent/tool → rerun affected slice**

Independent trials can also run in parallel to reduce wall-clock time without changing the evaluation methodology.

## Reproducibility requires versioning

A timestamped result folder is useful, but it is not enough.

A test run should record the versions and configuration of both the system being evaluated and the evaluator itself:

* dataset version
* selected tasks and tags
* agent/code version
* model and model configuration
* prompts and tool definitions
* grader/rubric versions
* trial count (k)

Otherwise “87 last week, 92 today” may be impossible to reproduce—or even interpret.

With versioned run configuration, historical evaluation becomes a trustworthy comparison of **quality, cost, latency, and reliability**.

## Closing

Offline evaluation turns agent development into engineering.

The essential pattern is straightforward:

**representative datasets → repeatable trials → deterministic checks → semantic grading → aggregates → traces → reruns**

The difficult part is defining “correct” without accidentally requiring one golden output or one golden tool path.

That is why the distinction between **facts, reference solutions, and assertions** matters. It lets an evaluator enforce what must be true while still allowing agents to find different valid solutions.

We built the Smart Agent Kit around that principle for DocRouter’s Document Agent. The medical insurance example shows that the same architecture can transfer to a very different domain.

If you are building custom agents, start collecting labeled cases early, measure every meaningful change, keep traces for debugging, track cost and latency alongside quality, and treat evaluation as part of the product rather than a one-off demo script.

## Further reading

* [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) — Anthropic Engineering

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
