```markdown
# pdf-craft Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill teaches the core development patterns and conventions used in the `pdf-craft` Python repository. You'll learn how to structure code, write and name files, manage imports/exports, and follow commit and testing standards. These patterns ensure consistency, maintainability, and clarity across the codebase.

## Coding Conventions

### File Naming
- Use **snake_case** for all file names.
  - Example: `pdf_parser.py`, `file_utils.py`

### Import Style
- Prefer **relative imports** within the package.
  - Example:
    ```python
    from .utils import parse_pdf
    ```

### Export Style
- Use **named exports** (explicitly define what is exported from a module).
  - Example:
    ```python
    __all__ = ['parse_pdf', 'extract_text']
    ```

### Commit Messages
- Follow the **Conventional Commits** standard.
- Use the `chore` prefix for routine changes.
- Keep commit messages concise (average ~68 characters).
  - Example:
    ```
    chore: update dependencies for security patch
    ```

## Workflows

### Code Contribution
**Trigger:** When adding or updating code in the repository  
**Command:** `/contribute`

1. Create a new Python file using snake_case naming.
2. Use relative imports for internal modules.
3. Define `__all__` for exported functions/classes.
4. Write clear, conventional commit messages (e.g., `chore: add PDF text extraction`).
5. If applicable, add or update a corresponding test file (`*_test.py`).

### Testing Code
**Trigger:** When verifying code correctness  
**Command:** `/test`

1. Identify or create a test file matching the pattern `*.test.*` (e.g., `parser.test.py`).
2. Write test functions for new or updated features.
3. Run tests using the project's preferred method (framework is unknown; check project docs or use `python <testfile>`).
4. Ensure all tests pass before committing changes.

## Testing Patterns

- Test files follow the pattern `*.test.*` (e.g., `pdf_parser.test.py`).
- The testing framework is not specified; check for test runners or use standard Python testing approaches.
- Place tests alongside or near the code they cover.

  Example test file:
  ```python
  # pdf_parser.test.py

  from .pdf_parser import parse_pdf

  def test_parse_pdf():
      result = parse_pdf('sample.pdf')
      assert result is not None
  ```

## Commands
| Command      | Purpose                                      |
|--------------|----------------------------------------------|
| /contribute  | Steps for contributing code changes          |
| /test        | Steps for writing and running tests          |
```
