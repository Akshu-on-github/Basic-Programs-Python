# First Contributions 🎉

Hey there! 👋 Want to contribute to open source? Here's a great guide to assist first-time contributors like you in making their first contribution to this project. 

## Step 1: Familiarize yourself with the repository 🧐
🔖 **Roles**  

These create an organizational structure for the project and are commonly found in open source projects.

| Role        | Description |
| ----------  |  ---------- |
| **Author**  | the person who created the project | 
| **Owner**   | administrative representative for repository or organization | 
| **Contributors** | people who contribute something to the project |
|**Maintainers** | people who are responsible for overseeing the project into its future goals |
|**Community Members** | users of the repository |

📚 **Documents** 

Documentation structures information in the repository. Sometimes, there might be sub-teams within a repository that have their own "team" document. Here are some common documents you will see in this project and possible others:

| Document        | Description |
| ----------  |  ---------- |
| **LICENSE**  | a required file that details the project's open-source license | 
| **README**   | go-to instruction manual that explains the project and its goals to new community members | 
| **CONTRIBUTING** | details the contributing process, guidelines, and types of contributions needed |
|**FIRST_CONTRIBUTIONS** | instruction manual to guide first-time contributors through the open-source project |
|**CODE_OF_CONDUCT** | establishes project rules to ensure the project is a welcoming environment. Please abide by them. |

🛠️ **Tools**

These organize discussions among contributors and community members. Check out some archived issues to understand how this community works. After, find an issue that you can contribute to, comment that you are interested in the issue thread, and an repository adminstrator will assign the role to you.

| Tool        | Description |
| ----------  |  ---------- |
| **Issues**  | allows people to discuss their experience with certain features in the project | 
| **Pull Requests**   | where contributor changes are reviewed by project administration | 

## Step 2: Git Installation 💻
Git allows you to save your contributions on your machine, update your copy of the repository to ensure you have the latest version, and push your changes to the open-source project.
1. Follow these instructions to install Git onto your machine **[here](https://help.github.com/articles/set-up-git/)**

## Step 2: Fork the repository ⚡ 
Forking makes a copy of the repository, so you can edit files on your local machine without interrupting the workflow of the project. 
1. Click the `Fork` button at the top of this page.

## Step 3: Clone the repository ⤵️
Cloning a repository makes a copy of the repository on your local machine. 

1. Open the forked repository in your GitHub account.
2. Click the green `Code` button
3. Click the 📋 clipboard symbol to copy the link
4. Open your terminal on your machine
5. Paste the following git command:
     ```
     git clone "URL you just copied
     ```
## Step 4: Make a new branch 🌱
Branches in Git are quite similar to that of a tree. They isolate specific code changes you made in a project, which can be helpful if you are adding a new feature to an existing product.
1. Move to the repository on your machine utilizing the following command:
     ```
     cd Basic-Programs-Python
     ```
2. Now that you are in the repository on your computer, you need to create a branch. Try to keep your branch name relevant to the project. Use this command and replace your branch name with `<insert-your-branch-name-here>` in the code block:

     ```
     git checkout -b <insert-your-branch-name-here>
     ```
     * For example: `git checkout -b add-luke-skywalker`

## Step 5: Make your code changes and commit them 🚧
If you selected an issue to work on (see Tools for more information), this is where you would make any changes you need to fix the issue.
1. Navigate through the repository on your machine and make necesary changes.
2. Check what files were modified using `git status`, and make sure they align with what you worked on. For changes that were not added to your branch yet, their file names will be red:
     ```
     git status
     ```
4. Save your changes onto the the branch you just created using the following command:
     ```
     git add <file-name> 
     ```
5. Once you add your changes, you can type `git status` again. For changes that you did add, the file name will be green.
6. Next, you need to commit your changes, so they are ready to be pushed back to the repository you are contributing to. Utilize the following command to do so:
     ```
     git commit -m "add a commit message here"
     ```
     * commit messages: make a short line describing what the change is (e.g. fixed login styling). In case if something goes wrong in the future, you can go through your commits, see what each chunk of changes were for, and go back to when your project was working.

## Step 6: Push your contributions to GitHub 🚀
While your changes are stored on your local machine, you need to push them back to the repository, so all community members can see them too.
1. Push your changes utilizing the following command:
     ```
     git push origin <your-branch-name>
     ```
## Step 7: Make a pull request 📈
Finally, you will need to submit your changes to review. Once they are reviewed by the repository leads, your changes will be added to the repository. If you open the repository on GitHub, you will notice a green `Compare & pull request button` button. 
1. Click the `Compare & pull request button` on GitHub.
2. Follow the repository's guideline for submitting a pull request, which may include adding information in the `Leave a comment` section of your pull request.
     * check the [CONTRIBUTING.md](https://github.com/Akshu-on-github/Basic-Programs-Python/blob/master/CONTRIBUTING.md/#opening-a-pr) for more information
3. Soon, the repository leads will merge 🔀 your changes into the repository. You will receive an email notification when your changes are merged. 

## Step 8: Celebrate! 🥳
Congratulations! You just made your first contribution to open source on the `Basic-Programs-Python` repository. The steps you just went through are standard for most open source projects (*fork -> clone -> add changes -> pull request -> changes merged)

So, now what? Check out other open source projects on GitHub that interest you and contribute to them. Your open source journey has just begun! ✨ 
