# fizzy_chess_server_v2
This is a flask based web server application that deals with the all server side handling of the chessWithFizzy app. 
</br>__*WOW*__

</br>

<!-----
NEW: Check the "Suppress top comment" option to remove this info from the output.

Conversion time: 1.234 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β30
* Tue Jul 20 2021 03:44:38 GMT-0700 (PDT)
* Source doc: backend access link - server & client communications (BAL-S&CC) protocol
* Tables are currently converted to HTML tables.

WARNING:
You have 3 H1 headings. You may want to use the "H1 -> H2" option to demote all headings by one level.

----->


<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 1; ALERTS: 0.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p>
<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>



# Client to Server Requests -


## <span style="text-decoration:underline;">Request structure</span> -  


```
        All client requests contain the Head of the request, the Body of the request, and the Meta of the request. 
```



        **The Head` - contains the Request Number.`**


        **The Body` - contains the request details as per each request code's specifications. If there is a mismatch between the request code and the Body an error message will be returned.`**


        **The Meta` - contains the Auth Cookie. In the case a client hasn't logged in yet this contains None. `**The` Auth Cookie will be formatted that each element is separated by the char '|' in the following order "username|pwd_hash|time_issued`|`expiration_time"`


        **The Auth Cookie` - a `**JSON` file containing the name and hashed password of the user. It also contains, time issued, cookie id, and expiration time. `


## 
    <span style="text-decoration:underline;">Queue Requests - </span>


### 
        <span style="text-decoration:underline;">Terms Used -</span> 


            **Time format(str)` - The time format the player wants to play with. Ex: "3+1".`**


            **Rating(int)` - The `**Elo` rating of the` `requesting player. Ex: 1345. `


            **CPU(bool)` - Whether the player wants to play against the AI or not.`**


<table>
  <tr>
   <td><code>Request Name</code>
   </td>
   <td><code>Request Number</code>
   </td>
   <td><code>Description </code>
   </td>
   <td><code>Body Structure </code>
   </td>
  </tr>
  <tr>
   <td><code>Queue Up</code>
   </td>
   <td><code>101</code>
   </td>
   <td><code>Request the server </code>for the player to<code> be added to the queue of players </code>
   </td>
   <td><code>f"{</code>,<code>time_format},</code>
<p>
<code>{rating},</code>
<p>
<code>{cpu}"</code>
   </td>
  </tr>
  <tr>
   <td><code>Queue Down</code>
   </td>
   <td><code>102</code>
   </td>
   <td><code>Request the server to be removed from the queue of players </code>
   </td>
   <td><code>f"{,time_format},</code>
<p>
<code>{rating},</code>
<p>
<code>{cpu}"</code>
   </td>
  </tr>
  <tr>
   <td><code>Check Match</code>
   </td>
   <td><code>103</code>
   </td>
   <td><code>Request to check if a match exists or has been found </code>
   </td>
   <td><code>f"{,time_format},</code>
<p>
<code>{rating},</code>
<p>
<code>{cpu}"</code>
   </td>
  </tr>
</table>



## Game Requests - 


### 
        Terms Used -


            **Game ID** - The identifying number of the current game given to the client by the server before the match starts. 


<table>
  <tr>
   <td><code>Request Name</code>
   </td>
   <td><code>Request Number</code>
   </td>
   <td><code>Description</code>
   </td>
   <td><code>Body Format</code>
   </td>
  </tr>
  <tr>
   <td><code>Check Board </code>
   </td>
   <td><code>201</code>
   </td>
   <td><code>Request from the server the current board state, the state of the game, and times.</code>
   </td>
   <td><code>f"</code>,<code>{game_id}"</code>
   </td>
  </tr>
  <tr>
   <td><code>Push Move</code>
   </td>
   <td><code>202</code>
   </td>
   <td><code>Request the server to push a move to the current board state and update times. </code>
   </td>
   <td><code>f",{game_id}"</code>
   </td>
  </tr>
  <tr>
   <td><code>Resign </code>
   </td>
   <td><code>203</code>
   </td>
   <td><code>Request from the server to resign the game.</code>
   </td>
   <td><code>f"{,game_id}"</code>
   </td>
  </tr>
  <tr>
   <td><code>Offer Draw</code>
   </td>
   <td><code>204</code>
   </td>
   <td><code>Request the server to offer the other player a draw. </code>
   </td>
   <td><code>f"{,game_id}"</code>
   </td>
  </tr>
  <tr>
   <td><code>Time Up</code>
   </td>
   <td><code>205</code>
   </td>
   <td><code>Request the server to resign the game due to time on the clock running out</code>
   </td>
   <td><code>f"{,game_id}"</code>
   </td>
  </tr>
  <tr>
   <td>Get Available moves
   </td>
   <td>206
   </td>
   <td>Request the server for available moves from the current position 
   </td>
   <td>f”{game_id}”
   </td>
  </tr>
</table>



## User Management Requests - 


### 
        Terms Used - 


            **Username` - The name of the user. `**


            **Hashed Password `- The password of the used hashed using hash256`**


<table>
  <tr>
   <td><code>Request Name</code>
   </td>
   <td><code>Request Number</code>
   </td>
   <td><code>Description</code>
   </td>
   <td><code>Body Format</code>
   </td>
  </tr>
  <tr>
   <td><code>Login</code>
   </td>
   <td><code>301</code>
   </td>
   <td><code>Request from the server to log in.</code>
   </td>
   <td>f<code>"{user_name}</code>_<code>{</code>pwd<code>}"</code>
   </td>
  </tr>
  <tr>
   <td><code>Logout </code>
   </td>
   <td><code>302</code>
   </td>
   <td><code>Request the server to be logged out. </code>
   </td>
   <td><code>None</code>
   </td>
  </tr>
  <tr>
   <td><code>Deadman Switch</code>
   </td>
   <td><code>303</code>
   </td>
   <td><code>Request the server to update it's deadman switch timer. </code>
   </td>
   <td><code>None</code>
   </td>
  </tr>
  <tr>
   <td>Sign Up
   </td>
   <td>304
   </td>
   <td>Request the server to create a new user account
   </td>
   <td>f”{username}_{pwd}”
   </td>
  </tr>
</table>



# 


# Server Returns - 

	`Invalid Request for 10x requests - 1000, f"{head}: {body}"`


```
    Hereon listed the returns for each Request number. 
```



## 
    101 queue up- 


<table>
  <tr>
   <td><code>Return Name </code>
   </td>
   <td><code>Return Number</code>
   </td>
   <td><code>Return body</code>
   </td>
  </tr>
  <tr>
   <td><code>Already in queue </code>
   </td>
   <td><code>1013</code>
   </td>
   <td><code>None</code>
   </td>
  </tr>
  <tr>
   <td><code>Still looking </code>
   </td>
   <td><code>1012</code>
   </td>
   <td><code>None</code>
   </td>
  </tr>
  <tr>
   <td><code>Success, Match Found</code>
   </td>
   <td><code>1011</code>
   </td>
   <td>f”{game_id}, {color}”
   </td>
  </tr>
  <tr>
   <td><code>General Failure </code>
   </td>
   <td><code>1014</code>
   </td>
   <td><code>None</code>
   </td>
  </tr>
</table>



## 102 queue down- 


<table>
  <tr>
   <td><code>Return Name</code>
   </td>
   <td><code>Return Number</code>
   </td>
   <td><code>Return Body</code>
   </td>
  </tr>
  <tr>
   <td><code>Not In Queue</code>
   </td>
   <td><code>1022</code>
   </td>
   <td><code>None</code>
   </td>
  </tr>
  <tr>
   <td><code>Success</code>
   </td>
   <td><code>1021</code>
   </td>
   <td><code>None</code>
   </td>
  </tr>
  <tr>
   <td><code>General Failure</code>
   </td>
   <td><code>1023</code>
   </td>
   <td><code>None</code>
   </td>
  </tr>
</table>



## 103 Check Match- 


<table>
  <tr>
   <td><code>Return Name</code>
   </td>
   <td><code>Return Number</code>
   </td>
   <td><code>Return Body</code>
   </td>
  </tr>
  <tr>
   <td><code>Not In Queue</code>
   </td>
   <td><code>1032</code>
   </td>
   <td><code>None</code>
   </td>
  </tr>
  <tr>
   <td><code>Success, Match Found</code>
   </td>
   <td><code>1031</code>
   </td>
   <td>f”{g<code>ame_id}</code>, {color}”
   </td>
  </tr>
  <tr>
   <td><code>Match Not Found</code>
   </td>
   <td><code>1033</code>
   </td>
   <td><code>None</code>
   </td>
  </tr>
  <tr>
   <td><code>General Failure</code>
   </td>
   <td><code>1034</code>
   </td>
   <td><code>None</code>
   </td>
  </tr>
</table>


Invalid Request- 2000,  `2000, f"{head}: {body}"`


## 201 - 


<table>
  <tr>
   <td>Return Name
   </td>
   <td>Return Number
   </td>
   <td>Return Body
   </td>
  </tr>
  <tr>
   <td>Not In Game 
   </td>
   <td>2012
   </td>
   <td>None
   </td>
  </tr>
  <tr>
   <td>Success
   </td>
   <td>2011
   </td>
   <td>f”{board_state_png}|{black_time}|{white_time}|{game_state}”
   </td>
  </tr>
  <tr>
   <td>General Failure
   </td>
   <td>2013
   </td>
   <td>None
   </td>
  </tr>
</table>



## 202 -


<table>
  <tr>
   <td>Return Name
   </td>
   <td>Return Number
   </td>
   <td>Return Body
   </td>
  </tr>
  <tr>
   <td>Not in Game
   </td>
   <td>2022
   </td>
   <td>None
   </td>
  </tr>
  <tr>
   <td>General Failure
   </td>
   <td>2023
   </td>
   <td>None
   </td>
  </tr>
  <tr>
   <td>Success
   </td>
   <td>2021
   </td>
   <td>f”{gave_check}”
   </td>
  </tr>
</table>



## 203 -


<table>
  <tr>
   <td>Return Name
   </td>
   <td>Return Number
   </td>
   <td>Return Body
   </td>
  </tr>
  <tr>
   <td>Success
   </td>
   <td>2031
   </td>
   <td>f”{new_rating}”
   </td>
  </tr>
  <tr>
   <td>Not in game 
   </td>
   <td>2032
   </td>
   <td>None
   </td>
  </tr>
  <tr>
   <td>General Failure
   </td>
   <td>2033
   </td>
   <td>None
   </td>
  </tr>
</table>



## 204- 


<table>
  <tr>
   <td>Return Name
   </td>
   <td>Return Number
   </td>
   <td>Return Body
   </td>
  </tr>
  <tr>
   <td>Success
   </td>
   <td>2041
   </td>
   <td>None
   </td>
  </tr>
  <tr>
   <td>Not in game 
   </td>
   <td>2042
   </td>
   <td>None
   </td>
  </tr>
  <tr>
   <td>General Failure
   </td>
   <td>2043
   </td>
   <td>None
   </td>
  </tr>
</table>



## 205 -


<table>
  <tr>
   <td>Return Name
   </td>
   <td>Return Number
   </td>
   <td>Return Body
   </td>
  </tr>
  <tr>
   <td>Success
   </td>
   <td>2051
   </td>
   <td>f”{new_rating}”
   </td>
  </tr>
  <tr>
   <td>Not in game 
   </td>
   <td>2052
   </td>
   <td>None
   </td>
  </tr>
  <tr>
   <td>General Failure
   </td>
   <td>2053
   </td>
   <td>None
   </td>
  </tr>
</table>



## 206 - 


<table>
  <tr>
   <td>Return Name
   </td>
   <td>Return Number
   </td>
   <td>Return Body
   </td>
  </tr>
  <tr>
   <td>Success
   </td>
   <td>2061
   </td>
   <td>f”{moves}”
   </td>
  </tr>
  <tr>
   <td>Not in game 
   </td>
   <td>2062
   </td>
   <td>None
   </td>
  </tr>
  <tr>
   <td>General Failure
   </td>
   <td>2063
   </td>
   <td>None
   </td>
  </tr>
</table>


Invalid Request- 3000,  `3000, f"{head}: {body}"`


## 301 -


<table>
  <tr>
   <td>Return Name
   </td>
   <td>Return Number
   </td>
   <td>Return Body
   </td>
  </tr>
  <tr>
   <td>General Failure
   </td>
   <td>3012
   </td>
   <td>None
   </td>
  </tr>
  <tr>
   <td>Success
   </td>
   <td>3011
   </td>
   <td>f”,{username}|{hashed_pwd}|{time_issued}|{cockie_id}|{exp_time}”
   </td>
  </tr>
</table>



## 302 -


<table>
  <tr>
   <td>Return Name
   </td>
   <td>Return Number
   </td>
   <td>Return Body
   </td>
  </tr>
  <tr>
   <td>Success
   </td>
   <td>3021
   </td>
   <td>None
   </td>
  </tr>
  <tr>
   <td>Not logged in
   </td>
   <td>3023
   </td>
   <td>None
   </td>
  </tr>
  <tr>
   <td>General Failure
   </td>
   <td>3022
   </td>
   <td>None
   </td>
  </tr>
</table>



## 303 -


<table>
  <tr>
   <td>Return Name
   </td>
   <td>Return Number
   </td>
   <td>Return Body
   </td>
  </tr>
  <tr>
   <td>Incorrect Password
   </td>
   <td>3033
   </td>
   <td>None
   </td>
  </tr>
  <tr>
   <td>General Failure
   </td>
   <td>3032
   </td>
   <td>None
   </td>
  </tr>
  <tr>
   <td>No account under username
   </td>
   <td>3034
   </td>
   <td>None
   </td>
  </tr>
  <tr>
   <td>success
   </td>
   <td>3031
   </td>
   <td>None
   </td>
  </tr>
</table>



## 304 -


<table>
  <tr>
   <td>Return Name
   </td>
   <td>Return Number
   </td>
   <td>Return Body
   </td>
  </tr>
  <tr>
   <td>Account Exists 
   </td>
   <td>3042
   </td>
   <td>None
   </td>
  </tr>
  <tr>
   <td>General Failure
   </td>
   <td>3043
   </td>
   <td>None
   </td>
  </tr>
  <tr>
   <td>success
   </td>
   <td>3041
   </td>
   <td>None
   </td>
  </tr>
</table>



    	

