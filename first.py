test1="""As a junior high school student, I began to learn programming. Unfortunately, I had read several junk
books, such as 21 Days Mastery C++, which were common at that time. It was not a big problem to read them,
and even to write a little program. But I don't know why the software is out of order. I can't start with
a slightly huge programming problem, and I can't do anything with the existing libraries. Although I code
constantly every day, I find myself programmed so slowly that I have only a very limited understanding of
the concepts of iteration and recursion, so to speak, just using a computer as a calculator.
After entering college, I majored in physics. For the first time, I had been memorizing and reciting the
physical formulas, but I couldn't understand how they came to be, what they were related to, or what they
meant. I kept learning how to calculate and answer some common physics questions, but I didn't know what
was behind these houses.
And when I tried to do some computer games based on physical behavior, I had the same problem again: I
couldn't get started with new problems, the fear of new problems grew, and I began to take the initiative
to escape, not really understand, but to fantasize about solving problems by copying and pasting code
through Google search. Fortunately, a class in my sophomore year completely changed my way of learning. It
was the first time that I had the feeling of "opening my eyes" and I realized painfully that I had only a
poor real understanding of some subjects, including physics and computer science minors.
About that lesson: We had just finished studying electricity and special relativity. The professor wrote
down the two subjects on the blackboard and drew a line to connect them. "Suppose we have an electron
moving along the wire at a relativistic level. At first the professor wrote down the familiar formulas of
electrical and special relativity, but after the algebraic derivation of several blackboards, the formula
for the magnetic field magically appeared. Although I knew this formula a few years ago, I had no idea
there was such a potential connection between these phenomena. The difference between magnetism and
electricity was just an "angle of view." I suddenly realized that I was no longer just pursuing how. I
began to ask why. I began to look back and pick up the basics and learn what I should have learned before.
This process of return is painful. I hope you can wake up and never do such a foolish thing."""
test2="""When I first started in junior high school, I started programming. Unfortunately, I read a few of the
garbage books that were common at the time, such as "21 Days Proficient in C++". At the time, I finished
reading it, and even wrote a small book. program. But the software has failed. I don't know why, the
slightly large programming problem can't be started, and the things that can't be done by the existing
library can only be spread. Although I keep coding every day, I find that my programming skills are so
slow to improve. I have only a very limited understanding of the concepts of "iteration" and "recursion".
It can be said that I just use the computer as a calculator.
After entering the university, I majored in physics. For the first time, I have been memorizing the
physical formulas, but I don't understand how they came out, what is the connection between them, or their
meaning. I keep learning how to calculate and answer some common physical problems, but I don't know
anything about the Why behind these How.
When I tried to do some computer games based on physical behavior, I encountered the previous difficulties
again: I couldn’t start with new problems, and the fear of facing new problems continued to grow. I
started to evade, not really Understand, but fantasy can solve the problem by copying and pasting the code
through Google search. Fortunately, a lesson in my sophomore year completely changed my approach to
learning. That was the first time I had the feeling of "opening the eye". I was painfully aware that I had
only a few poor real understandings of some disciplines, including the computer science of my major in
physics and minors.
About that class: At that time we just finished studying the content of electricity and special
relativity. The professor wrote these two themes on the blackboard and drew a line to connect them.
"Assume that we have an electron moving along the wire at a relativistic level..." At the beginning, the
professor simply wrote the common formulas of electricity and special relativity that we are familiar
with, but after the algebraic derivation of several blackboards, the formula of the magnetic field The
magic has appeared. Although I already knew this formula a few years ago, I didn't know at the time that
there was such a potential connection between these phenomena. The difference between magnetism and
electricity is only the problem of "observation angle". I suddenly realized that I will not only pursue
what to do afterwards. I started to ask why (wy), I started to look back and pick up the most basic ones.
Partly, learn the knowledge that I should have learned before. This process of turning back is painful. I
hope that you can wake up and never do this stupid thing."""
test1=test1.replace(',','').replace('.','')
test2=test2.replace(',','').replace('.','')
test1=test1.split()
test2=test2.split()
print(test1)
print(test2)
setword1=set(test1)
setword2=set(test2)
for i in setword1:
    count=test1.count(i)
    print(i,'test1出现次数：',count)
for i in setword2:
    count=test2.count(i)
    print(i,'test2出现次数：',count)
