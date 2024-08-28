### Metadata Project Proposal

# Project Introduction
The motivation behind this project stems from the observed disparity in the representation of non-Western language works within online databases.  Inadequacy in the metadata associated with these works leads to incomplete search results, particularly noticeable when searching for works by authors from regions such as Southeast Asia. This deficiency not only harms a researchers' ability to access certain works, but also reflects a broader societal issue of unequal treatment of non-Western authors. The primary target audience for this project includes researchers who utilize HathiTrust and similar online databases. The project aims to address the problem of fragmented metadata by consolidating identical works with varying metadata into a unified and comprehensive format.

# Project Methods
Our approach involves parsing through MARC database files, containing a subset of metadata from the sources under consideration. Python will serve as the primary programming language for parsing and processing this information. Familiarity with MARC record tags is crucial for mapping tags to corresponding metadata fields accurately. The dataset will undergo sorting and grouping using open-source algorithms, such as the Levenstein distance to accurately determine the similarity of two works, and to identify similar works based primarily on author and title metadata. Additional metadata fields will contribute to this process but to a lesser extent. Under time constraints, the idea of adding additional fields will come at a later time. Discrepant metadata will be segregated for further comparison as more data becomes available. Addressing metadata accuracy challenges such as misspellings or inaccuracies will involve leveraging the UM-GPT API to evaluate the compiled results.  This effort will be consolidated into a "master list" categorizing identical works along with their aggregate metadata, presented as a user-friendly .txt file output.

# Expected Results/Findings
The project aims to foster transparency and collaboration by making the program open-source through a GitHub repository accessible to all. A comprehensive README.md file will accompany the repository, providing detailed documentation of the code. As this project is primarily student-led, each team member seeks to gain expertise in working with Language Model-based algorithms like UM-GPT, metadata management, and product development from inception to execution. While the project's results are achievable by human efforts, the automation facilitated by this initiative significantly expedites the process, making it feasible within a reasonable timeframe.

# Project Scope
The scope of the current project is to identify and eliminate duplicates within the dataset, focusing on ensuring uniqueness based on author, title, and publication date. By accomplishing this task, searching and retrieval of unique works within an online database will become more efficient for researchers. Future plans for the project involve the incorporation of additional metadata fields, such a work’s subject fields, and addressing transliteration challenges for non-Western works. These objectives serve as potential next steps for the project. Incorporating subject fields will primarily occur during the removal of duplicates of the project. The idea is that if two identical works have different metadata, the differences between them will be added to the “master list”, enriching the metadata fields for that specific work. Tackling the transliteration problem will include reverse engineering Roman scripts back into their native language, which will aid researchers conducting research on non-western works.

![Slide6](https://github.com/user-attachments/assets/b81124a1-2f17-4303-8196-fd978a43527b)


