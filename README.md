# gptscript-nyx

A sample project using gptscript to chat with Nyx.

Nyx is a revolutionary, decentralised application that addresses the principal challenge adopting Generative AI within enterprise: secure, trusted access to domain-specific, contextualised and real-time data. Nyx brings together communities of proprietary data producers and data consumers in a secure, transparent, and user-friendly environment.

Data producers and data consumers come together in a Nyx formed network to exchange AI ready data.

## This poc

[GPTScript](https://github.com/gptscript-ai/gptscript) is a tool that allows easy integrations of LLMs with various sytems (local executables, remote APIs, etc).

Bringing Nyx and GPTScript together is a proof that the two tech can integrate well and complement each others.

To prove the integration, the project defines a agent (`agent.gpt`) acting as a chatbot who's been provided with a set of tools that wrap access to Nyx. As a result, a user can basically chat with Nyx as a data consumer by searching the Nyx network for new and interesting data products to be discovered and - where allowed - subscribed to, browse and interrogate the subscribed products and download them locally. 

This POC is complementary to GPTScript own [Local Files Demo](https://github.com/gptscript-ai/local-files-demo) that allows CSV files to be interrogated.

## Status

This is a proof of concept to learn GPTScript and make use of Nyx via its SDK.

## Structure

- **agent.gpt** the main chatbot script. 
- tools:
    - **nyx-discoverer**: search the nyx network for products that match the user prompt
    - **nyx-my-data**: browse the subscribed products
    - **nyx-downloader**: downloads one or more products

## How to run it

Pre-requisites:

- Install [gptscript](https://github.com/gptscript-ai/gptscript)
- Install Python 3.11 or above.

Then:

1. install the [nyx-client](https://pypi.org/project/nyx-client/) in a local environment and generate the nyx credentials file following the instructions in the "First Time Setup" section.
    - the credentials file is stored in the `.env` file
1. run the agent remotely
    - run `gptscript --workspace . github.com/smartrics/gptscript-nyx` assuming that the `.env` file is in the current directory or adjust the argument of the `--worspace` flag to the directory where the Nyx `.env` file is
1. run the agent locally
    - clone `github.com/smartrics/gptscript-nyx`
    - create and activate a python venv
    - run `pip install -r requirements.txt`
    - follow the steps above to create the `.env` file
    - run `gptscript agent.gpt`
