import gym

# utworzenie srodowiska cartpole-v1
e = gym.make('CartPole-v1', render_mode = 'rgb_array')

# środowisko nalezy zawsze zresetowac i zapisujemy w obs (obserwacje)
obs = e.reset()


print(f'''

obserwations - lista obserwacji: 
      
{obs} 

----

action_space - possible moves. In cartpole we have 2 possible moves left or right, 1 or 0: 

{e.action_space}

---

observation_space: 

{e.observation_space}

---

step - for step(0) we've moved cartpole to the left. We got 4 items:
1. new observation assembled from 4 numbers
2. reward which i 1
3. done flag with value False, which means that the episode haven't finished yet
4. additional information about the environment, so empty dictionary

{e.step(0)}

      ''')

e.render()