---
layout: post
title: "How To Create Document Workflows With Temporal And DocRouter.AI"
date: 2025-12-25 00:00:00 +0000
author: "Andrei Radulescu-Banu"
image: /assets/images/temporal_docrouter_workflows.svg
categories: [tech, programming, ai, tutorials]
---

Processing large multi-page documents with AI requires careful orchestration. When documents are hundreds of pages long, they can't be processed in a single LLM prompt due to token limits. This post describes a real-world implementation that uses [Temporal](https://temporal.io/) to orchestrate document processing workflows with [DocRouter.AI](http://docrouter.ai), solving the specific problem of extracting patient information from surgery schedule documents.

The implementation is available at [doc-router-temporal](https://github.com/analytiq-hub/doc-router-temporal) and processes surgery schedule documents containing hundreds of pages, extracting patient names, dates of birth, and medical insurance information.

## Table of Contents

- [The Problem: Large Multi-Page Documents](#the-problem-large-multi-page-documents)
- [Why Temporal for Document Chunking and Processing?](#why-temporal-for-document-chunking-and-processing)
- [The Solution: A Multi-Stage Workflow](#the-solution-a-multi-stage-workflow)
- [Creating Schemas and Prompts with Claude Agent](#creating-schemas-and-prompts-with-claude-agent)
- [The Complete Workflow Implementation](#the-complete-workflow-implementation)
- [Development Process](#development-process)
- [Key Implementation Details](#key-implementation-details)
- [Results and Next Steps](#results-and-next-steps)

## The Problem: Large Multi-Page Documents

Surgery schedule documents can contain hundreds of pages, with each page potentially containing:
- Medical insurance card
- Pre-operative documentation
- Anesthesia records
- Other records

The challenge is that these documents are too large to process in a single LLM prompt. Modern LLMs have token limits (typically 128K-200K tokens), and a 200-page PDF can easily exceed these limits when converted to text. Even if it fits, processing the entire document at once is inaccurate.

The solution requires:
1. **Chunking**: Split the PDF into individual pages
2. **Classification**: Identify which pages contain insurance card vs pre-operative evaluations vs. anesthesia records vs other patient information
3. **Grouping**: Group patient pages by patient (using name and DOB as keys)
4. **Extraction**: Extract structured data from each patient set of pages, including insurance card information

<div data-excalidraw="/assets/excalidraw/document_processing_solution.excalidraw" class="excalidraw-container">
  <div class="loading-placeholder">Loading diagram...</div>
</div>
<div style="text-align: center; margin-top: 1rem;">
  <a href="/excalidraw-edit?file=/assets/excalidraw/document_processing_solution.excalidraw" target="_blank" style="color: #2563eb; text-decoration: none; font-weight: 500;">
    📝 Edit in Excalidraw
  </a>
</div>

## Why Temporal for Document Chunking and Processing?

[Temporal](https://temporal.io/) provides durable workflow orchestration that's perfect for this use case:

- **Durable execution**: If a worker crashes while processing 200 pages, Temporal resumes from where it left off
- **Parallel processing**: Process multiple pages simultaneously while maintaining order
- **Error handling**: Automatic retries for transient failures (API rate limits, network issues)
- **State management**: Track which pages have been processed, which patients have been identified, etc.
- **Long-running workflows**: The entire process can take minutes to hours, and Temporal handles this gracefully

Traditional approaches (queues, background jobs, or simple scripts) struggle with:
- Maintaining state across hundreds of operations
- Handling partial failures (what if page 150 fails but pages 1-149 succeeded?)
- Coordinating parallel processing with proper error handling

## The Solution: A Multi-Stage Workflow

The implementation uses a hierarchical workflow structure:

1. **Classify and Group PDF Pages** (`ClassifyAndGroupPDFPagesWorkflow`): Chunks the PDF, classifies each page, and groups pages by patient
2. **Extract Insurance Information** (`ClassifyGroupAndExtractInsuranceWorkflow`): Creates patient-specific PDFs and extracts insurance card data

The workflow processes documents in these stages:

```
Large PDF (200+ pages)
    ↓
[Chunk into individual pages]
    ↓
[Classify each page: surgery schedule vs. insurance card vs. other patient information]
    ↓
[Group patient pages by patient (first_name, last_name, DOB)]
    ↓
[Create patient-specific PDFs]
    ↓
[Extract insurance card information for each patient]
    ↓
[Return structured results]
```

### Workflow Diagram

Here's a visual representation of the complete workflow:

<div data-excalidraw="/assets/excalidraw/temporal_docrouter_workflow.excalidraw" class="excalidraw-container">
  <div class="loading-placeholder">Loading diagram...</div>
</div>
<div style="text-align: center; margin-top: 1rem;">
  <a href="/excalidraw-edit?file=/assets/excalidraw/temporal_docrouter_workflow.excalidraw" target="_blank" style="color: #2563eb; text-decoration: none; font-weight: 500;">
    📝 Edit in Excalidraw
  </a>
</div>

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

## Creating Schemas and Prompts with Claude Agent

Before building the Temporal workflow, we needed to create the extraction schemas and prompts that DocRouter.AI would use. This was done using the **Claude Agent for DocRouter.AI**, which is implemented as an MCP (Model Context Protocol) server.

The Claude Agent implementation is located at [`doc-router/packages/typescript/mcp`](https://github.com/analytiq-hub/doc-router/tree/main/packages/typescript/mcp) and consists of:

- **CLAUDE.md**: Instructions for Claude Code on how to use DocRouter MCP tools
- **MCP Server** (`src/index.ts`): TypeScript implementation that provides tools for creating schemas and prompts in DocRouter.AI

### Using the Claude Agent

With the Claude Agent, you can prompt Claude Code to create extraction schemas and prompts. For example:

```
Create a schema for extracting patient information from surgery schedule pages.
The schema should include:
- First name
- Last name  
- Date of birth
- Address (street, city, state, zip)
- Insurance information (provider, policy number, group number)
```

The Claude Agent uses the MCP tools to:
1. Validate the schema structure
2. Create the schema in DocRouter.AI
3. Create associated prompts for extraction
4. Test the extraction on sample documents

This approach allows rapid iteration on schema and prompt design without writing code. The schemas and prompts created this way are then used in the Temporal workflow activities.

For this implementation, we created:
- **`anesthesia_bundle_page_classifier`**: A prompt that classifies pages as surgery schedule, patient information, or other
- **`insurance_card`**: A prompt that extracts insurance card information from patient pages

## The Complete Workflow Implementation

The main workflow is `ClassifyGroupAndExtractInsuranceWorkflow`, which orchestrates the entire process. The complete implementation is available in [`workflows/classify_group_and_extract_insurance.py`](https://github.com/analytiq-hub/doc-router-temporal/blob/blog_post_dec_2025/workflows/classify_group_and_extract_insurance.py).

### Step 1: Classify and Group Pages

The workflow first calls `ClassifyAndGroupPDFPagesWorkflow` as a child workflow. This workflow:

1. **Chunks the PDF** into individual pages using `read_and_chunk_pdf_activity`
2. **Uploads each page** to DocRouter.AI with the classification tag
3. **Waits for classification** to complete for all pages
4. **Groups pages** by patient using `group_classification_results_activity`

The grouping activity is particularly interesting - it extracts patient information (first name, last name, DOB) from each page's classification results and groups pages by patient key (format: `firstname_lastname_YYYY_MM_DD`). The complete implementation is in [`activities/group_classification_results.py`](https://github.com/analytiq-hub/doc-router-temporal/blob/blog_post_dec_2025/activities/group_classification_results.py).

The grouping logic includes:
- **Name normalization**: Handles various name formats and case variations
- **DOB parsing**: Supports multiple date formats and normalizes to `YYYY_MM_DD`
- **Fuzzy matching**: Uses Levenshtein distance to merge patients with similar names (typos, abbreviations)

### Step 2: Create Patient-Specific PDFs

For each patient group, the workflow creates a new PDF containing only that patient's pages. The complete implementation is in [`activities/create_and_upload_patient_pdf.py`](https://github.com/analytiq-hub/doc-router-temporal/blob/blog_post_dec_2025/activities/create_and_upload_patient_pdf.py).

This activity:
1. Reads the original PDF file
2. Extracts the specified pages using PyPDF2
3. Creates a new PDF with only those pages
4. Uploads it directly to DocRouter.AI (avoiding passing large binary data through Temporal)

### Step 3: Extract Insurance Information

After all patient PDFs are uploaded and processed, the workflow polls for completion and then retrieves the insurance card extraction results for each patient.

## Development Process

The Temporal workflow was developed in **Cursor**, iterating 3-4 times over the implementation. The development process involved:

1. **Initial implementation**: Basic workflow structure with chunking and classification
2. **Adding grouping logic**: Implementing patient grouping with name/DOB matching
3. **Insurance extraction**: Adding the second stage to extract insurance card information
4. **Error handling and retries**: Adding proper error handling and retry logic

The total implementation time was **2 days**, which demonstrates how quickly you can build complex document processing workflows with Temporal and DocRouter.AI.

## Key Implementation Details

### Avoiding Large Data Transfer Through Temporal

One important design decision: we avoid passing large binary data (PDF bytes) through Temporal. Instead:

- PDFs are read from disk in activities (not in workflows)
- Patient PDFs are created and uploaded directly to DocRouter.AI
- Only document IDs and metadata flow through Temporal

This keeps Temporal workflow history small and efficient.

### Parallel Processing

The workflow processes multiple patients in parallel. Each patient PDF is created and uploaded independently, and the workflow polls for all of them concurrently.

### Error Handling

The implementation includes:
- **Retry logic**: Failed document processing is retried up to `max_retries` times
- **Status polling**: The workflow polls document status until completion or timeout
- **Graceful degradation**: If insurance extraction fails for a patient, the workflow still returns patient information without insurance data

## Results and Next Steps

The implementation successfully processes surgery schedule documents with hundreds of pages, extracting:
- Patient names, dates of birth, and addresses
- Medical insurance card information
- Surgery schedule page identification

The workflow is production-ready and handles:
- Large document processing (200+ pages)
- Parallel patient processing
- Error recovery and retries
- Long-running operations (minutes to hours)

### Running the Workflow

To run the workflow, see the [README](https://github.com/analytiq-hub/doc-router-temporal/blob/blog_post_dec_2025/README.md) and the [client script](https://github.com/analytiq-hub/doc-router-temporal/blob/blog_post_dec_2025/client_classify_group_and_extract_insurance.py):

```bash
# Start the Temporal worker
python worker.py

# In another terminal, run the client
python client_classify_group_and_extract_insurance.py <path_to_pdf>
```

The workflow returns a JSON structure with:
- `file_name`: Original PDF filename
- `pages`: Classification results for all pages
- `schedule`: List of surgery schedule page numbers
- `patients`: Dictionary mapping patient keys to patient data including insurance card information

## Conclusion

This implementation demonstrates how Temporal and DocRouter.AI work together to solve real-world document processing challenges. The combination provides:

- **Reliability**: Durable workflows that survive crashes and handle errors gracefully
- **Scalability**: Process hundreds of pages in parallel
- **Flexibility**: Easy to iterate on schema and prompt design using the Claude Agent
- **Speed**: Complete implementation in just 2 days

The code is available at [doc-router-temporal](https://github.com/analytiq-hub/doc-router-temporal/tree/blog_post_dec_2025) for reference and adaptation to your own document processing needs.

For more information:
- [Temporal Documentation](https://docs.temporal.io/)
- [DocRouter.AI Documentation](https://docrouter.ai/docs/quick-start)
- [DocRouter.AI MCP Server](https://docrouter.ai/docs/mcp)
