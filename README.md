# Descrription

A toy version of Claude Code using Google's Gemini API.



> [!WARNING]
> The agent can run arbitary code in the specified directory
> This program is a toy project for learning and doesn't have all the security and safety features that a production AI agent would have.
> This is for learning purposes only! Run at your own risk.


The agent has access to calculator directory and can execute code within it.
You can give it prompts to inspect or run the files.
If you introduce some simple bugs to the calculator code base (like changing operator precedence)
the agent should be able to fix the bugs and test your code. It can either run the code to make sure
that certain issue is fixed or run the unit tests.

Currently the agent is only allowed to call the functions from functions directory.


# Set-up

## Install UV

Linux
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Check the command for your system at https://docs.astral.sh/uv/getting-started/installation/

## Sync

```
uv sync
```

Create .env file in the root of the project and provide `GEMINI_API_KEY` variable.

## Run

```
uv run main.py "<user_promt>
```

```
uv run main.py "<user_promt> --verbose
```


## Example

```
uv run main.py "Fix the bug: 3 + 7 * 2 shouldn't be 20. Inspect pkg/calculator.py to find the error"


 - Calling function: get_file_content
 - Calling function: write_file
Final response:
I've fixed the bug in `pkg/calculator.py`. The issue was with the operator precedence for addition.
I've updated the `precedence` dictionary to set the precedence of `+` to 1, which is lower than `*` (2).
This ensures that multiplication is performed before addition, so "3 + 7 * 2" will now correctly evaluate to 17.
```