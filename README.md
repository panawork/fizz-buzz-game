# fizz-buzz-game
FizzBuzz game 

<h2>Summary</h2>
<p>Overral this project took about 27 hours in total as I started on the 17th Februrary and everyday I would work on it for about 1-3 hours,
at first I created the first archive to try it with only 2 players, it took a bit of time as I had to research how the players turns could switch each time
and then I was able to use 2 while loops since it was only 2 players, furthermore, I created a 2nd archive to try and adapt this code into more players, specifically
how many players the user wanted, this one took 3 hours or more because I had to use a list and try and understand how to add a player depending on the amount the user wants,
fortunetely I ended up finding a way by using a for loop that uses the range of the number of players which is what the user inputs and then it appends the names of the players.
Now in order to loop through each player I had to create an index and whilst the game is running the index will plus 1 switching to the next player after the player inputs their answer.</p>

<p>In my 3rd archive is where I started implementing object-oriented-programming techniques where I created a class called FizzBuzz and where I used self to create variables and use them in all the methods,
at first I kept getting errors because it seemed like I didnt understand how the classes work but after a lot of research I managed to understand how it works and hence managed to make it work for the project.
For the 4th archive I wanted to add more stuff in, I wanted to add a score and lives and then plus or take away based on the answers the players have given, at first I was really confused because I started it out with
dictionaries and it didn't seem to work so I was struggling alot, until I remembered about double lists, so i had the original player list be plain and then when the user specifies how many players they want it would 
automatically add double lists for each one, in each of those double list using the for loop it would automatically add the 'name', the score (set 0) and the lives (set 3) with this new implementation I now added extra code into the main game method of the class where if the player got it right it would plus 1 to the score and if they got it wrong it would take away 1 life, and if they ran out of lives the player would then get eliminated.</p>

<p>the very last archive being called officialgame is where I finally finished everything, I managed to even add a timer where if a user takes more than 5 seconds after they input their answer it would mention that they
were too late and would immediately eliminated them, I tried using theading but I was still not as confident with that library so for now I just focused on using the time module and it did work, for my very own bonus idea
I created a custom command where when the user types in "py officialgame.py --cheatmode" it would enter into a cheatmode and show the answers for everyone which took me abit of time but in the end I managed to do it.
Overral this project has helped me alot as I was able to learn alot more and I will continue making more.</p>

<h2>How to use</h2>
<p>The game will ask how many players, based on how many you input it will ask for the names, after you have set the names it will start automatically,
the count starts from 1 and if the number is divisible by 3 you type in "fizz" if its divisible by 5 you type in "buzz", if its divisible by both you
type in "fizzbuzz" and if its not divisible by any of them then you just type in the answer. However, each question has a time limit of 5 seconds and 
if you take longer then it will eliminated you from the game.</p>
<h3>Example</h3>
<p>"the count is 1" - Type in 1</p>
<p>"the count is 3" - Type in "fizz"</p>
<p>"the count is 5" - Type in "buzz"</p>
<p>"the count is 15" - Type in "fizzbuzz"</p>

<h2>command list</h2>
``` --cheatmode
```
<h3>Example</h3>
<p>"py officialgame.py --cheatmode"</p>

<h2>Installation requirements</h2>
<p>pip install pyfiglet</p>
<p>pip install colorama</p>
