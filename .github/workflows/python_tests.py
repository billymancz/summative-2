# This is a GitHub Actions workflow file that defines a CI pipeline.
# It will automatically run your Python unit tests on every push
# and pull request to the 'main' branch.

name: Python Unit Tests

# Controls when the workflow will run
on:
  # Triggers the workflow pull request events but only for the "main" branch
  pull_request:
    branches: [ "main" ]

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Step 1: Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - name: Check out repository code
        uses: actions/checkout@v4

      # Step 2: Sets up the Python environment
      - name: Set up Python 3.10
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      # Step 3: (Optional but recommended) Install any dependencies if you had them
      # For this project, there are no external dependencies, but if you had a
      # requirements.txt file, you would install them here like this:
      # - name: Install dependencies
      #   run: |
      #     python -m pip install --upgrade pip
      #     pip install -r requirements.txt

      # Step 4: Run the unit tests using Python's unittest module
      - name: Run tests with unittest
        run: |
          python -m unittest discover -v
