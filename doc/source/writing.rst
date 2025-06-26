.. _writing:

My writing communication guide. Clear - Simple, Concise (CSC)
-------------------------------------------------------------

I rarely join calls these days. There are two reasons. The first is time zone differences. I'm in South Korea. Most work is done between 9 AM and 5 PM in the US, which is 9 PM to 5 AM here. The second reason is to protect my daily dose of mental capacity for creative work. I primarily serve the role of a producer. Whether I like it or not, my brain sets aside some of its resources to prepare for incoming real-time human interaction. After the call, my brain is exhausted, which could have otherwise been used for useful work. I can replace the majority of real-time human interactions with writing. For developing `scikit-package <https://github.com/scikit-package/scikit-package>`_, which consists of 6-8 GitHub repositories with Prof. Simon Billinge, I don't recall having a single call. Features, releases, architectures, and design decisions were communicated in writing.

Writing is timeless. Writing enables us to work asynchronously. Through our written words, we can provide value to the organization we belong to and the community we are a part of. Whether it's a GitHub issue, a research manuscript, or a work email, I present a framework that I adopt to amplify the impact of my writing. Before I present the framework, I list the **core principles of writing** that guide it.

Core principles
~~~~~~~~~~~~~~~

- **Writing reflects the internal state of the author.** Whether written in the first or third person, it reveals the author's understanding of the subject and emotional state at the time of writing.
- Similarly, written words are read, interpreted, and evaluated by readers whose experiences and emotional states vary at the time of reading.
- **Writing is not the goal.** It's a medium, one of many ways to communicate. The goal is to **benefit from the act of writing**. In emotionally charged situations, a face-to-face conversation may be more effective. But when writing is the chosen medium, every word should be carefully selected and positioned to provide value for the organization's mission.
- **Writing reflects the degree of respect.** Reading consumes time and energy. Our time is valuable and limited. Good writing respects the reader's and the organization's collective time and resources.
- **Writing democratizes decision-making.** Unlike verbal communication, which carries tone, accent, and social cues that may introduce bias, writing—especially when using standard language—can help foster a more decentralized exchange of ideas. This is important for organizations where truth-seeking matters, such as in academic research or open-source software development.

1. Clear
~~~~~~~~

Being clear means the reader can take **decisive action based on the written words**. In software development, this might mean merging a pull request, sharing an opinion on a feature request, or deciding whether to include a new feature in the upcoming release. In manuscript writing, it could mean deciding whether to include an additional figure, add a co-author, or add new references. **To avoid writing too much, the writer must assume the reader's level of knowledge and provide the minimum amount of information required for decision-making**. Anything beyond what is needed to make that decision may be considered disrespectful of the reader's time.

However, we must be careful. What the author considers clear may not be clear to the reader. **A textbook can be condensed into a cheatsheet, but a cheatsheet can't be expanded into a textbook.** Don't share a cheatsheet when the reader actually needs PDF lecture notes instead. Writing clearly means considering the reader's perspective and providing the necessary context, problem, and solution. This is especially important in open-source software development, where the reader may not share the same background or context as the author or the core maintainers.

Whether to share a textbook, cheatsheet, lecture note, video link, image, or all depends on the reader. It is the full responsibility of the writer, not the reader, to provide the most optimal content for the reader to make a decision.

2. Simple
~~~~~~~~~

The next step is to **simplify** the writing. Here, simplify means to reduce the cognitive load on the reader. In other words, **it makes the ideas stick.** We've all sat through technically solid presentations that were ultimately forgettable because they were too complex. Clear writing that is also simple is much more memorable. Real-world examples help. When I introduced :ref:`principles`, I used a toothbrush analogy to show how transforming a conscious activity into a subconscious one frees up the mind. While it can be quite an abstract concept, familiar objects and human behaviors help crystallize an abstraction into something tangible.

When I was trying to make our ``scikit-package`` tutorial friendly and lower the activation energy for first-time users, I found it more effective to write “I want to release my package” rather than “Do you want to release your package?” That small shift reduces the reader's cognitive load—they don't have to mentally translate “you” into “I.” Both are clear, but one is more accessible and simple to search and remember if the user returns later to find the exact tutorial section they need.

3. Concise
~~~~~~~~~~

We are at the final stage. Our words are clear so the reader can make a firm decision. Our words are simple so the reader can recall our ideas. The last step is to be economical with our words. **Concise writing is about using the fewest words possible to convey the intended meaning.** It respects the reader's time and attention, allowing them to quickly grasp the key points without unnecessary fluff.

It caters to the core principle above of respect. Brevity respects the reader's time, attention, and energy. If we refer to the same concept often, introduce acronyms (e.g., ``cf`` for ``conda-forge``, ``skpkg`` for ``scikit-package``). Another is to choose precise words over long phrases. It is important to use the terms that are defined by GitHub, including ``origin`` and ``upstream``, instead of writing "the forked repository" or "the original repository." While both are equally clear and simple, we want to use the terms that are defined so that our communication can scale and also save time.

In the end, writing isn't just a tool for communication. It's a reflection of how we think and how we show respect for others. Let **Clear, Simple, Concise**—in that order—be our guide for writing anything professionally. Of course, many of these principles apply primarily to software development and scientific writing.

Exceptions and questions
------------------------

There is one exception when the **principles should be violated**: often, emotion is more important than being clear, simple, and concise. The framework lacks the human side of it. Hence, we have to be mindful that "Joy is the driving force." This is further discussed in :ref:`open-source-leadership`.

Here are some questions I ask when I am about to write and refine so that I and readers can benefit from the act of writing:

    - What are the 3 core principles of writing? How are they ordered in terms of importance?
    - Have I provided the minimum amount of information yet sufficient context (code snippets, tables, charts, screenshots, images, figures, examples, anecdotes) to allow the reader to make a decision? (Principle #1)
    - Have I presented simpler user behavior and experience so that the reader can remember? (Principle #2)
    - Have I used the specific jargon or terms used in the community, given that the reader is familiar with the terms? (Principle #3)
    - What's the limitation of the Clear, Simple, Concise framework in writing?

*First draft: Jun 26, 2025 (Incheon, South Korea)*
