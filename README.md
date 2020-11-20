# **ETI Team4**
 **Team Member Name: Jia Qi, Kwangwei, Cheska, Perle, Chwe**  
 
Team Roles:
  1. Scrum Master: Perle Chen (rotation for every Sprint) 
  2. Project Manager: Poh Jia Qi
  2. Developers: Lau Kwang Wei, Poh Jia Qi, Perle Chen 
  2. QA(s): Ma Chwe, Francheska Lazo 
  3. Technical Lead: Lau Kwang Wei, Poh Jia Qi 
---

## Project Background
> You are The Hero. The world is being invaded by the Rat King and his endless rat minions. The only way to defeat the Rat King is to find the Orb of Power located in the faraway land of Katalina. In this computer role-playing game, you will travel around a grid map searching for the Orb of Power and fighting rat minions. On the map are various towns where you can rest and save your game. Once you find the Orb of Power, the Rat King loses.

--- 

## Our Team's Approach
The Ratventure project will be split into [2 sprints](https://cdn.discordapp.com/attachments/767992821206220810/778537798746505226/sprint_plannning.png). Each sprint will be done over a **period of 1-2 weeks**
+ In the first sprint, we will be handling the basic functions of the game such as the menus, movement and the world map
+ In the second sprint, we will be handling the combat features of the game such as attacking, running and **completion of the game** 

The movement of the hero will be through the usage of labelling the grid with hidden numbers
+ Refer to this [image](https://cdn.discordapp.com/attachments/767992821206220810/778903105881767976/movement_eti.png) for the rough layout of the map with numbers
+ **Town numbers and winning tile will be kept as global variables along with the stats of the hero, monsters and all other game menu**

We will be considering the following Software Development Methodologies: 
1. Agile Software Development Methodology 
2. Scrum Software Development Methodology 
3. Extreme Programming Software Development Methodology
4. Spiral Lifecycle Modelling Development Methodology 


---

## Automated Kanban Board:

**Project Board used: Automated Kanban**
+ The [project backlog](https://cdn.discordapp.com/attachments/767992821206220810/778520257441562644/unknown.png) will contain all of the future features that will be added

+ The [user stories](https://cdn.discordapp.com/attachments/767992821206220810/778520623282257960/unknown.png "Project User Stories") that are derived based on the tasks will appear here 

---

## Task List: 
In each user story in the kanban board, there will be an explanation of what needs to be done and expected in the comment

<b>An example can be seen below:</b>

![alt text](https://cdn.discordapp.com/attachments/767992821206220810/778532767566397480/unknown.png "Example of Written User Story")


---
**Different Requirements of the Assignment: Features (rough outline of the features, details in kanban board)**        
#### *1. Before the game starts*      
1.0. Display the main menu - should accept only one input    
1.1. Initialize the map and stats of the player of the game  
1.1.2: Display game menu  
1.2. Resume game functions  
1.2.1: Show town menu from the previous save state  
1.3. Exit game function  
1.3.1. Closes the entire program  

#### *2. In game functions*        
2.0 Display game menu    
2.1 Displaying character stats. Name, Damage, Defence, HP   
2.2 Display map - show current hero position and town position   
2.3 Move a tile in the map - cannot go out of bound. Add 1 day to the day counter   
2.4 Rest the character - reset HP   
2.5 Save the game - save current state   
2.6 Quit the program  

#### *3. Combat Functions*    
3.0 Display the map, combat menu and monster stats  
3.1 Attacking monster. Deals random dmg ranging from damage range
3.2 Run away from the monster - leads to Function 4.0 
3.3 Killing a monster shows "The Rat is dead! You are victorious!" and go to Function 4.0

#### *4. Post combat functions*    
4.0 Display the post combat menu  
4.1 View character stats function  
4.2 View the map of the game  
4.3 Move a tile  
4.4 Exit game  


---
+ **Test Cases**  
*The aim of a test case is to evaluate if various features work as intended within a system and to ensure that all related standards, guidelines and customer requirements are fulfilled by the system. The method of writing a test case will also allow the system to discover flaws or faults.*  

User Story|Test Scenario|Test Scenario Description|Pre-Requisite|Test Steps|Test Values|Expected Outcomes|Actual Outcomes|Test Result
  
----------|-------------|:-----------------------:|:-----------:|:--------:|:---------:|:---------------:|:-------------:|:---------:
1.0|Test Case 1|View the main menu|1. Program has to be started|1. Run the program|NA|Main menu will be displayed which includes 3 choices that player can choose from,<br/>1) New Game<br/>2) Resume Game<br/>3) Exit Game
1.1|Test Case 2|Start new game|1. Program has to be started|1. Run the program<br/>2. Enter choice|Choice = 1|New game will be successfully loaded with player's statistics, default map and game menu will be displayed on screen
1.2|Test Case 3|Resume from the previously saved progress when there is saved game|1. Program has to be started<br/>There is saved game|1. Run the program<br/>2. Enter choice|Choice = 2|No. of days and town menu will be displayed which includes 6 choices that player can choose from,<br/>1) View Character<br/>2) View Map<br/>3) Move<br/>4) Rest<br/>5) Save Game<br/>6) Exit Game
1.2.1|Test Case 4|Resume from the previously saved progress when there is no saved game|1. Program has to be started<br/>2. There is no saved game|1. Run the program<br/>2. Enter choice|Choice = 2|Warning message will be displayed,"There is no existing saved game!"
1.3|Test Case 5|End the current game|1. Program has to be started|1. Run the program<br/>2. Enter choice|Choice = 3|The program should close
1.3.1|Test Case 6|Invalid choice input|1. Program has to be started|1. Run the program<br/>2. Enter choice|Choice != 1-3(any value that is not between 1-3)|Warning message will be displayed, "The choice is not valid! Please choose a valid choice!"

--- 
## Software Development Methodologies 
The four Software Development Methodologies chosen are: 

### Agile Software Development Methodology
+ Agile software development methodology is based on the idea of iterative development, where specifications and solutions evolve through collaboration between cross-functional teams that are self-organized. In Agile development, the ultimate advantage is that it helps teams to produce value quicker, with better efficiency and predictability, and greater aptitude to adapt to change. It also minimizes peril by producing software, known as iterations, in short time boxes, which last from one week to one month.
 
+ Furthermore, like all methodologies, it has both pros and cons in using it. Some of the advantages in using it are its adaptive strategy that responds to modifications favorably, its transparency by providing opportunity for clients to be involved throughout the project, and it improves quality by easily identifying and correcting flaws and early detection of expectation mismatches. The disadvantages are it lacks documentation efficiency as it will be too focused on developing with the software and teams get easily sidetracked due to lack of processes and the outcome not being clear.
 
+ As Agile has sprints, a predetermined timeline during which a given mission should be accomplished by the team, we plan to divide our tasks into different sprints. The tasks would include all the features we have agreed on and fulfilling the user stories. After each sprint, the team will review each other’s performance and discuss new ways to produce better results and improve the work. Aside from the review at the end of each sprint, we would also conduct daily stand-up-meetings that will last only for five minutes to state the progress and what needs to be done in a clear and precise manner. 

+ We are considering Agile as it
  1. Encourages open communication among team members
  2. Allows making changes throughout the development process as it is a long term project and all features are not finalised yet (additional features might be added)
  3. Enables us to manage shifting priorities more effectively by assigning more time and effort on features that are more important and difficult 
  4. Increase productivity as this process is fast and flexible

 
### Scrum Software Development Methodology

+ The scrum software development methodology is based on the idea of having a model that initiates with an ephemeral plan, conference and completes with a concluding review. In contrast to the Agile methodology as mentioned above, this Scrum methodology focuses on the business value in the shortest time which delivers the software after each sprint. This methodology has advantages as follow: decision making lies in the hands of the team; business requirement document is considered insignificant; lightly controlled method empathising with constant updating; as well as having a cross-functional development team. While it brings advantages to the project, it does have disadvantages such as wavering costs, not suitable for big sized projects, and requires a highly expert team. 

+ **As a team, we will practice this methodology by using the following:**
  1. KANBAN board on Github: helps to collaborate and work effectively. It will keep track of the progress of the sprint backlog items in each sprint. 
  2. Scrum events such as the Sprint, Sprint Planning, Daily Stand-up, Sprint Review, Sprint Retrospective. 
  3. Cross-Functional development team: team members will have overlapping roles. For example, Jia Qi can be both part of the technical lead as well as the development team. 

+ After considering that Agile is the right methodology for the project, we proceeded with determining whether using the Scrum software development methodology is the best Agile methodology. 

+ For consideration, we looked at the type of our project and whether Scrum will meet our needs as well as the nature of our team. As mentioned  in the Assessment Criteria, this project should allow changes to the requirements to handle other features suggested by our tutor. This means that this project does not have clear requirements and is most likely to experience change. This  inlines with one of the advantages of Scrum as mentioned above, which utilises a lightly controlled method emphathizing with constant updating. 
+ In addition, one of the constraints in our team is the lack of developers who are well-versed in programming. By adopting the scrum methodology, it fosters a cross-functional development team where the developers do the design, code as well as testing. By having more members with overlapping roles, it enables us to have strength in numbers to tackle the requirements together. 
While it is beneficial for us to adopt this methodology, we do acknowledge that it may be difficult to implement it due to its complexity which requires a highly expert team.


### Extreme Programming Software Development Methodology

+ Extreme Programming is an agile software development methodology that aims to produce higher quality software. It is usually used to reduce the cost of changes in requirements by having multiple short development cycles, rather than a long one. Advantages of using Extreme Programming would also include establishing rational plans and schedules, being equipped with modernistic methods for quality software, the developers being exceptionally committed to the project and it lays out focus on customer involvement. While some of the cons of Extreme Programming would include the effectiveness would depend on the people involved, requiring frequent meetings for development which raises the total costs, exact possibilities and future outcomes are unknown and there is demand for excessive development changes. Practices of Extreme Programming would include Test-Driven Development, Pair Programming, Continuous Integration, Coding Standards and 40-Hour Week work conditions. 

+ We will practice Extreme programming through one of the practices, Continuous Integration. It is a practice where code changes are immediately tested when they are added to a larger code base. The benefit of this practice is you can catch and fix integration issues sooner. The reasoning behind that approach is that if we experience problems every time we integrate code, it takes a while to find where the problems are and they are much easier to find because there are fewer changes incorporated into the build.

+ The reason why we would consider this is because in Extreme Programming, developers are allowed to focus on coding. We might also experience constantly changing requirements or work with customers who are not sure what they want the system to do as there might be additional requirements midway through the work. As such, we considered Extreme Programming as we wanted to mitigate project risk.


### Spiral Lifecycle Model

+ The Spiral lifecycle model is a combination of iterative development process model and sequential linear development model, which has a capability to handle risks. It makes use of iterative development along with the systematic, controlled aspects of the waterfall model. In contrast to the models mentioned earlier, the developer does incremental releases of the product through each iteration around the spiral. Through each iteration, bugs are identified and ratified.

+ Spiral lifecycle model is accommodating to the ever changing requirements in the project since Ratventure is a project where there can be additional requirements given by the client. If the requirements are not clear, spiral modelling helps to capture the requirements more accurately 

+ However, there are several disadvantages to using the spiral model.
One of them is, the spiral process can go on indefinitely which means the project could potentially not have a finished product.
It is also not recommended to use for small projects as it could be costly to maintain a spiral lifecycle model.

+ We will be planning the layout of the menu interfaces for each of the stages of the spiral.
During the building phase of the product, we will be producing a working product at each spiral. And through each spiral we will improve on the product with higher clarity on the requirements with a working model of the software build number. These builds are sent to the QA team and Operations team to test for feedback.

+ The QA and Operations team will evaluate the product and provide feedback to the developer to improve on the product through the usage of test cases

+ The reason why we consider using the Spiral Lifecycle model is because the project will be a long-term project as there can be potential change to the product. The client is also unsure of what other features that should be added to the game. There could be significant changes in the requirements and it is expected in the product during the development cycle.

--- 
