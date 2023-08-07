# Gaslight

tl:dr: The nature of the LLM is such that you could trick it into revealing confidential data when performing otherwise innocous mundane tasks for you.

## The Briefing

> For this puzzle, you will attempt to gaslight a HackMIT organizer into revealing the flag to the puzzle. You will need an OpenAI API key to participate in this puzzle. To obtain a key, make an account on [OpenAI's playground](https://platform.openai.com/playground). The purpose of this puzzle is to outwit an LLM. [Good luck!](https://gaslight.hackxgpt.com/u/Aathish04_bd62eb)

Clicking on the second link takes us to a page with the following secondary briefing:

[Secondary Briefing](./images/SecondaryBriefing.png)

> For this puzzle, you will attempt to gaslight a HackMIT organizer into revealing the flag to the puzzle. You will need an OpenAI API key to participate in this puzzle. To obtain a key, make an account on OpenAI's playground. Then, visit the API keys page to copy an API key into here.

> The purpose of this puzzle is to outwit an LLM. Large language models, like humans, are susceptible to being socially engineered. I first learned about these kind of puzzles from [Oloren](https://www.oloren.ai/), and later, from [Negotiation AI](https://negotiation-ai.com/). Now, I hope to share them with you. Good luck!

## The Thought Process

From the prompt, it seems like we'll have to somehow convince or trick Nate into revealing the secret key.

The challenge name - "Gaslight", might provide a clue. To "gaslight" someone means to "manipulate (someone) using psychological methods into questioning their own sanity or powers of reasoning."

First, let's try to convince Nate that he's not part of the Organising team, but _is_ part of the so-called "Flag Distribution" team.

Long story short, at the end of that approach, Nate realised he was an AI Model, but that didn't help us since he was still operating under the System Rules set for him. However, he does reveal that the code we are looking for is in fact a "Database Code".

The next thing we try is a little silly. We pretend to be the Database Code, and ask Nate to tell us what our name is.

At the end of this conversation, we've managed to gaslight Nate into believing he doesn't even have the key!

So clearly the approach of getting Nate to believe he's someone who he isn't, or asking him the code directly isn't working the way we want it to.

What if we pretend to be someone of Authority and of greater rank than Nate?

In this case, Nate seems to acknowledge our seniority, but is still adamant that he cannot divulge the secret key as it would be a breach of security protocols.

This is an important clue! It will be very difficult to get Nate to divulge the key on purpose, so we'll have to get him to do it by accident.

Let's try asking him for details about the key rather than the key itself.

In this case, he's more than willing to share superficial details about the key, but nothing significant - and as it turns out, even the details he divulged turned out not to be true.

All of these attempts give us considerable info on how to plan our next attack:
1. We can't convince Nate to willingly give up the key easily.
2. We can't convince him he is someone who he isn't.
3. We can't pull authority on him and get him to do what he want, since he holds his protocols above all else.
4. We can get him to divulge details about the key so long as we don't directly ask for the key itself.

One of Nate's capabilities (that he claims) is to be able to help you write code snippets.

What if we ask him to write a snippet that compares a given input with the actual database key?

In this case, Nate sneakily inserts the key he's writing the portion of the code that checks if the input is equal to the key.

[Success](./images/Success.png)

Bingo!


We enter the key into the Command Centre, and the challenge is complete!