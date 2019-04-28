# kdd_cup 2019

# Data description
l  Query record. A query record represents one route search from a user on Baidu Maps. Each query record consists of a session ID, a profile ID, a timestamp, coordinates of the original point, coordinates of the destination point. For example, [387056, 234590, "2018-11-01 15:15:36", (116.30,40.05), (116.35,39.99)] means a user makes a query on a trip from (116.30,40.05) to (116.35,39.99) in the afternoon of Nov. 1st, 2018. All coordinates are WGS84.

l  Display record. A display record is the feasible routes generated by Baidu Maps shown to the user. Each display record consists of a session ID, a timestamp and a list of route plans. Each display plan consists of the transport mode, the estimated route distance in meters, the estimated time of arrival (ETA) in seconds, the estimated price in RMB cent and implicitly the display rank in the display list. To avoid confusion, there is at most one plan of a specific transport mode in the display list. There are 11 transport modes in total. A transport mode could be unimodal (e.g., drive, bus, cycle) or multi-modal (e.g., taxi-bus, cycle-bus), we encode these transport modes into numerical labels range from 1 to 11. For example, [387056, "2018-11-01 15:15:40", [{“mode”:1, “distance”: 3220, “ETA”: 2134, “price”: 12}, {“mode”:3, “distance”: 3520, “ETA”: 2841, “price”: 2}]] is a display record of two transport mode plans.

l  Click record. A click record indicates the user feedback of different recommendations, i.e., a user may click on specific routes displayed to him/her for details. In each record, click data contains a session ID, a timestamp, and the clicked transport mode in the display list. We only preserve the first click for each query.

l  User attributes. User profile attributes reflect individual preference on transport modes. The user of each session is associated with a set of user attributes via a profile ID. Each profile record consists of a profile ID, a set of one hot encoded user profile dimensions. Note that for the privacy issue, we don’t directly provide physically individual user IDs. Instead, each user is represented as a set of user attributes and then users with same attributes are merged with the same user profile ID. For example, with gender and age attribute considered, two males of age 35 are identified as the same user in the dataset.

# preprocessing
主要是把['o','d','req_time']給區分好:  
(116.30,40.05) ---> 116.30 | 40.05  
req_time只取小時 :"2018-11-01 15:15:36" ---> 15  

# preprocessing2
針對plans去做處理  
plans:  
[{"distance": 22691, "price": 700, "eta": 4888, "transport_mode": 7}, {"distance": 21483, "price": "", "eta": 2303, "transport_mode": 3}, {"distance": 21483, "price": 5500, "eta": 2543, "transport_mode": 4}, {"distance": 21328, "price": 400, "eta": 6046, "transport_mode": 1}]  

切成44個col 因為總共有11種transport_mode  
mode1   dis1     price1     eta1   mode2 dis2 ... price11 eta11  
    1  21328        400     6046       0    0 ...       0     0  
 如果推薦有mode1 則mode1 填入1  有推薦mode3 則mode3 填入 1 其餘的mode填0  
 接者把有推薦的值分別輸入後面  
