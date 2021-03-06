## AI Pseudo-Code
```

Algorithm findRoute():
  current := startState
  frontier := [ current ]
  While frontier is not empty:
    Generate successors
    Remove current from frontier
    For Each successor:
      Generate wait durations
      Apply evaluation function
      Append successor to frontier
    current := node in frontier with min value
    If current is destination:
      Generate route
      Return

```
***
## Train Map
```

                  ,---------------17-------------[KLK]---15---[GWT]
          6-----[DEL]                            /
         /       \                              /
      [JPR]       5,                           /
       /      ,---[GWL]----------------------21
      /      /       \
    10      16        \
    /      /          17
   /      /            |
 [AMD]   /             |
   |    /              |
   7   /               |
    \ /                |
   [MUM]----------13   |
     \              \  |
      \            ,[HYD]
       20         /
        \        12
         \      /
          \    /                          |     [STATIONS]
           [BLR]-------18-------[VKP]     |    
             |                   /        |      0 - MUM
             6                  /         |      1 - DEL
             |                 /          |      2 - GWL
             |                /           |      3 - CHN
            [CHN]-----------12            |      4 - KLK
                                          |      5 - BLR
                                          |      6 - AMD
  +--------------------------------+      |      7 - HYD
  |  [ABC] = City                  |      |      8 - JPR
  |  --n-- = Journey Time (Hours)  |      |      9 - GWT
  +--------------------------------+      |     10 - VKP

```
***
## Data Fromat
```

      ---to-->
      c0 c1 c2 c3 c4 ..
 | c0 +------------- ..
fr c1 | actual costs,
 | c2 | sld's,
 | c3 | train schedules,
 v c4 | 
    : :

```
***
## Final Result Format
```

+-------------------+
| BLR - start       |
| departure: 1400   |
| elapsed: 0h       |
+-,-----------------+
  |
  |
+-'-----------------+
| MUM               |
| arrival: 1000     |
| departure: 1000   |
| elapsed: 20h      |
+-,-----------------+
  |
  |
+-'-----------------+
| GWL - end         |
| arrival: 0200     |
| elapsed: 36h      |
+-------------------+

```
***