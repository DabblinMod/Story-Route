class TreeNode:
#this tree NOde is going to keep track of two things
  #1 is a portion of the story
  #2 is the choices a user can make to progress the story

  def __init__(self, story_piece):
    self.story_piece=story_piece
    self.choices=[] #the user makes choices, choices holds the objects of each node
    
  def add_child(self, node):
      #each node in the tree is going to be a peice of the story
      if(node in self.choices):
        return #skip it / exit without adding
      self.choices.append(node) #otherwise add the node

  def traverse(self):
    story_node=self #tracks current portion of story
    print(story_node.story_piece)
    #while there are choices, until there are None, loop
    while(len(story_node.choices) > 0):
      #checks if there are choices through each loop
      #check if the choice user puts in is valid by using the num of choices
      choice=int(input("Enter 1 or 2 to continue the story: "))
      if(choice==0 or choice > len(story_node.choices)):
        #if the choice is greater than the number of options or less than, inform the user they haven't made a choice and force them to try again
        print("Invalid choice. Try again! Enter 1 or 2!")
        continue
        #change the current node to the choice you've made
      elif(choice > 0 and choice <= len(story_node.choices)):
        #subtract 1 from choice to get correct index
        choice_index=choice-1
        chosen_child=story_node.choices[choice_index]
        #story_node=story_node.choices[choice_index]
      else:
        return
      print(chosen_child.story_piece) #at the end print the story piece.
      story_node=chosen_child #Keep doing this until you have no more choices to make for the story / its end if so.
    print("THE END")
######
# VARIABLES FOR TREE
  user_choice=input("What is your name? ")
  print(user_choice)
######

######
# TESTING AREA
print("Once upon a time...")
story_root=TreeNode("""
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
""")
#print(story_root.story_piece)

choice_a=TreeNode("""
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
""")

choice_b=TreeNode("""
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
""")

choice_a_1=TreeNode("""
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.
 
YOU HAVE ESCAPED THE WILDERNESS.
""")

choice_a_2=TreeNode("""
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.
 
YOU REMAIN LOST.
""")

choice_b_1=TreeNode("""
The bear is unamused. They frown at you, and in a soft voice replies. "Yes, I CAN talk. How kind of you to notice."
 You are stunned into silence. After smelling the flowers, it turns around, glances your way once, then with a 'HMPH!', leaves you alone.
YOU REMAIN LOST. 
""")

choice_b_2=TreeNode("""
The bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.

With a smile, you thank the bear, and together, follow the path before splitting ways at the exit.
 
YOU HAVE ESCAPED THE WILDERNESS.
""")
story_root.add_child(choice_a)
choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)
story_root.add_child(choice_b)
choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)
story_root.traverse()
#print(story_root.story_piece)