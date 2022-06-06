from pyamaze import maze,COLOR,agent

m=maze(20,20)
m.CreateMaze(loopPercent=50,theme=COLOR.light)
a=agent (m,filled=True,footprints=True)
m.tracePath({a:m.path})
a=agent(m,shape='arrow',footprints=True)


m.run()