<script lang="ts">
  import { Marked } from 'marked';
  import { markedHighlight } from 'marked-highlight';
  import { gfmHeadingId } from 'marked-gfm-heading-id';
  import hljs from 'highlight.js';
  import 'highlight.js/styles/github-dark.css';

  const { content } = $props<{ content: string }>();

  // Create a new marked instance to avoid global state issues
  const marked = new Marked();

  // Configure marked with extensions
  marked.use(
    gfmHeadingId(),
    markedHighlight({
      langPrefix: 'hljs language-',
      highlight(code, lang) {
        const language = hljs.getLanguage(lang) ? lang : 'plaintext';
        return hljs.highlight(code, { language }).value;
      }
    })
  );

  marked.setOptions({
    gfm: true,
    breaks: true,
  });

  const htmlContent = $derived(marked.parse(content) as string);
</script>

<div class="markdown-renderer prose prose-lg prose-headings:text-tx50 prose-p:text-tx300 prose-li:text-tx200 prose-a:text-pm500 prose-a:no-underline hover:prose-a:underline prose-strong:text-tx100 prose-code:text-pm500 prose-pre:bg-bg200 prose-th:bg-bg200 prose-th:text-tx50 prose-td:text-tx200 prose-td:border-bg300 prose-tbody:text-tx200 prose-blockquote:border-l-pm500 prose-blockquote:text-tx200 prose-img:inline-block prose-img:m-0 max-w-none">
  {@html htmlContent}
</div>

<style>
  /* Badge layout - paragraphs with images displayed as flex */
  .markdown-renderer :global(p:has(> img:first-child)) {
    display: flex;
    flex-wrap: wrap;
    gap: 0.28rem;
    align-items: center;
    justify-content: center;
  }

  /* Force table text colors to be readable in dark mode */
  .markdown-renderer :global(table),
  .markdown-renderer :global(thead),
  .markdown-renderer :global(tbody),
  .markdown-renderer :global(tr),
  .markdown-renderer :global(td) {
    color: var(--color-tx200) !important;
  }

  .markdown-renderer :global(th) {
    color: var(--color-tx50) !important;
  }

  /* Details/summary elements */
  .markdown-renderer :global(details),
  .markdown-renderer :global(summary) {
    color: var(--color-tx200) !important;
  }
</style>
