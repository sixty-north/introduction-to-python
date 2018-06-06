Looks like we'll run this as a two-hour mini-workshop at NDC Oslo. Here's the rough plan...

1. Students will create accounts on pythonanywhere.com to run the code.
2. They'll use the bash console to git-clone the repo (this or another...not sure yet)
3. I'll do a quick intro and run-through of the notebook. This will be a good chance for them to get pythonanywhere going (i.e. create an account)
4. Once they've seen the program via the notebook, I'll direct them to the code
   in v01 and ask them create a new type of room. I'm thinking something that
   contains an instrument for soothing the bear. They can pick it up, go to the
   bear, play the instrument, and safely pet it. I'll probably need to introduct
   some dict syntax for this.
5. Then they'll transfer this work over to v02. This will means creating a new Python file.
6. Finally, we'll transfer that to v03. Here we'll learn about virtual
   environments. We'll install our program there and see that we can run it from
   anywhere.

Time permitting, I'd like to do something with the web as well. pythonanywhere
let's you run WSGI web apps pretty easily, so we'll need to update zaweb to use
flask instead of aiohttp. I think with this change we'll be able to run
everything. We'll probably want to provide a canned WSGI config, and likely even
a script for installing the WSGI config.
