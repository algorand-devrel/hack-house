This repo contains all of the developer-focused content from the Hyderabad Hack House held March 24-26, 2023.

# Run Steps

## Intro to AlgoKit
1. [slides](intro_to_algokit/Intro-to-AlgoKit-Hyderabad-Hack-House.pdf) (PDF)
2. install: `pipx install algokit`
    - detailed [Windows installation](https://www.youtube.com/watch?v=22RvINnZsRo) (video)
    - detailed [macOS installation](https://www.youtube.com/watch?v=zsurtpCGmgE) (video)
3. `algokit init`
4. `algokit localnet start`
5. `algokit localnet explore`

## Intro To Beaker
1. `cd intro_to_beaker`
2. `algokit bootstrap all` to install dependencies
3. `poetry shell` to enter shell with proper Python venv set
4. `python app.py` to build and interact with the smart contract

## Intro to JavaScript SDK
1. `cd intro_to_js_sdk`
2. `algokit bootstrap all` or `npm i` to install dependencies
3. `npx tsx index.ts` to run demo script
