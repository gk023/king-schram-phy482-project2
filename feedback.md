Names: Katie Schram and Garrett King

------

I will compile your feedback and scores for the pair projet into this document. Please don't alter this document.
Thanks, Danny

------

## Homework assignment 6

Feedback: Folks, I'm glad to give feedback on the poster and I do hope that you get your module working this week. First thing: there's a lot of text on your poster. Try to break up things into bullet points and give some space between things. You want to reduce the text so that it's a reminder of what is important, and not a prescription of what to say. This goes for the intro and the methods section. Also, what is a dynamo? You say you are looking into them, but don't say what they are and why the matter. I'd take some small space you get back from cutting text to say just a bit about them. The figures are fine, but the captions don't explain what we should get from them. I don't think the role of a figure is to convey what you did, but rather what sense should we make of the figure? Your method sections already says what you did. Depending on what you finish your conclusions should talk about what results you have and where things can go. It should be written like you are doing this for your research not for class. I'm glad that you got a lot out of it, but in the poster you are sharing your knowldge about modeling dynamos with pyro to your classmates, so take that framing. Make sure to put your names at the top, etc, because you might not be around when the poster first goes up. Good job getting this draft together this week.

* Score: 20/20

## Homework assignment 5

Feedback: I'm really glad to find that the issue was probably that the problem was stiff and that adapting the time step helped. I think you have a good plan and already have a reasonable set of figures and such to prepare a poster draft, which I would suggest that you try to do this week as it's the last week for formal feedback. Depending on what you find with the adaptive solution or the builtin integrator, you might have different things that you can present. One thing that will be critical will be explaining the equations in question and how you are solving them to produce solutions. You will want to aim this at your classmates, so they can understand what is going on and why this problem is being solved the way that it is. Great work this week!

* Score: 20/20

## Homework assignment 4

Feedback: Folks, I'm glad to see that you are getting something that works (at least for a short timescale). I'm also glad to see you trying to debug it and think about other resources that can help you with it. The kind of problem that you solving is sometimes the result of a stiff equation (https://en.wikipedia.org/wiki/Stiff_equation) where for some regime the problem can be solved easily, but then you get to a point where things change a lot you need a narrower window to solve it (i.e., an adaptive solution). This is because the errors you make compund really fast. Now that you have written things from scratch, you might compare this to a simple 4th order Runge-Kutta solver, which is a also easy to write (I have a book that you can use or you can google it) or a builtin scipy integrator (https://docs.scipy.org/doc/scipy-0.13.0/reference/generated/scipy.integrate.ode.html). Even if you don't solve this issue, it would be interesting to compare the different numerical approaches to find out what kind of issue you think you are having. A lot of computational research is finding or developing the right algorithm to control errors like this. It might not seem like it right now because it's not working, but you are doing good work that has to be done.

* Score: 20/20

## Homework assignment 3

Feedback: Folks, I'm glad to see you both working on this together. I think I have a much better idea of what you plan to do, but you might want to look into the Finite Difference Method and you might want to further restrict your problem. Some resources on solving PDEs numerically are here: https://ocw.mit.edu/courses/aeronautics-and-astronautics/16-920j-numerical-methods-for-partial-differential-equations-sma-5212-spring-2003/lecture-notes/ THere's some Python packages that could help you, but the finite difference method is also easy enough to code by hand. I have a book in my office that might also be of use to you and feel free to come by and look through it or borrow it. Solving MHD in general is really tough (ask the nuclear astro people!), so I want you to think about what's the simplest model that we cna solve with this and then what might be the next extension to it (if it's not enough). I'm worried about you still have a bit more of a complex project than I expect of you. Feel free to wow us, but also I don't want you to be overwhelmed. I'm looking forward to seeing your model next week, which will help me know where you are.

* Score: 20/20

## Homework assignment 2

Feedback: Folks, the plan that you have here works for me and helps me understand what you will be doing. It does appear that the responsbilities on the project haven't been parted out as much as they probably should be (i.e., who is going to do what) and this might become a problem later as you are working on this. I'm still also curious as to what you intend to model, but I guess you plan to think through that this week and share it. My reminder would be to aim small first and think about aspects that could be added on as you want.


* Score: 16/20

## Homework assignment 1

Feedback: Folks, this is a great idea for a project and definitely fits with the spirit of what I'm hoping you would do. I'm a bit concerned that this might be a little more than you can do in the given time, that is, this seems a bit ambitious. I'm hoping by next week you can narrow this down a bit to modeling some particular aspect - maybe the basic model of dynamos and how they work. It might be that we start there and expand into another area by adding a new feature to the model. This is a great idea, I just don't want you to do a PhD for this project.

* Score: 20/20
