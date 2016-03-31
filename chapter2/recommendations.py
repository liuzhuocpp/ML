#coding=utf-8
critics={

'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
              'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 
              'The Night Listener': 3.0},

'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 
                 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 
                 'You, Me and Dupree': 3.5}, 

'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
                     'Superman Returns': 3.5, 'The Night Listener': 4.0},

'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
                 'The Night Listener': 4.5, 'Superman Returns': 4.0, 
                 'You, Me and Dupree': 2.5},

'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
                 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
                 'You, Me and Dupree': 2.0}, 

'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                  'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},

'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}
}

print critics['Lisa Rose']['Lady in the Water']

from math import sqrt

#返回两个人的欧几里得相关度
def sim_distace(prefs, person1, person2):

    pref1 = prefs[person1]
    pref2 = prefs[person2]

    ans = 0

    
    for key, value in pref1.items():
        if pref2.has_key(key):
            ans += pow(pref1[key] - pref2[key], 2)

    ans = 1 / (1 + sqrt(ans));
    return ans;

print "%.17f" %sim_distace(critics, 'Lisa Rose', 'Gene Seymour')


#皮尔逊相关度
def sim_pearson(prefs, p1, p2):
    prefX = prefs[p1]
    prefY = prefs[p2]
    com = {}
    for key, val in prefX.items():
        if prefY.has_key(key):
            com[key] = 1

    sumX = sum([prefX[i] for i in com.keys() ] )
    sumY = sum([prefY[i] for i in com.keys() ] )

    print "SUM : " , sumX, sumY


    aveX = sumX / len(com)
    aveY = sumY / len(com)

    print "AVE : " , aveX, aveY




    tmp = [  (prefX[i] - aveX) * (prefY[i] - aveY) for i in com.keys()  ]
    print "TMP", tmp
    for i in com.keys():
        print "NAME", i
        print "SB", (prefX[i] - aveX), (prefY[i] - aveY)


    up = sum(tmp)

    print "UP : " , up, len(com)

    down_left = sum([ pow(prefX[i] - aveX, 2)  for i in com.keys()   ])
    down_right = sum([ pow(prefY[i] - aveY, 2)  for i in com.keys()  ])

    down = sqrt(down_left * down_right)
    if down == 0: return 0
    return up / down

print  "%.17f" %sim_pearson(critics,'Lisa Rose', 'Gene Seymour')







