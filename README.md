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


    