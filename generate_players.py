import numpy as np

def generate_stat_values(mean, std_dev, size):
    stats_values = np.random.normal(mean, std_dev, size)
    return stats_values

def loop_stat_list(stats, std_devs, size):
    ret_list = []
    i = 0
    for s in stats:
        ret_list.append(generate_stat_values(s, std_devs[i], size))
        i+=1
    ret_list_final = np.array(ret_list)
    return ret_list_final

#hgt,wgt,spd,str,tpw,tha,cth,blk,prh,bks,tck,cov,fiq,bcv,cry,kpw,kac
####### QB STATS SECTION #######
five_qb_stats_list   = [74,205,83,60,90,85,50,50,50,50,50,50,75,50,50,10,10]
five_qb_std_dev_list = [5,5,5,5,5,10,5,5,5,5,5,5,10,5,5,1,1]
qb_size = 5
five_qb_list = loop_stat_list(five_qb_stats_list, five_qb_std_dev_list, qb_size) 
print(five_qb_list)
################################

####### HB STATS SECTION #######
five_hb_stats_list   = [71,205,92,65,50,50,70,60,50,50,50,50,60,80,80,10,10]
five_hb_std_dev_list = [5,5,5,8,5,5,5,5,5,5,5,5,10,10,10,1,1]
hb_size = 10
five_hb_list = loop_stat_list(five_hb_stats_list, five_hb_std_dev_list, hb_size) 
#print(five_hb_list)
################################

####### WR STATS SECTION #######
five_wr_stats_list   = [70,205,92,60,50,50,85,50,40,40,40,40,60,70,70,10,10]
five_wr_std_dev_list = [8,5,5,5,5,5,5,5,5,5,5,5,10,8,8,1,1]
wr_size = 20
five_wr_list = loop_stat_list(five_wr_stats_list, five_wr_std_dev_list, wr_size) 
#print(five_wr_list)
################################

####### TE STATS SECTION #######
five_te_stats_list   = [76,245,87,70,50,50,83,65,40,40,40,40,60,60,60,10,10]
five_te_std_dev_list = [8,5,5,5,5,5,5,5,5,5,5,5,10,5,5,1,1]
te_size = 8
five_te_list = loop_stat_list(five_te_stats_list, five_te_std_dev_list, te_size) 
#print(five_te_list)
################################

####### OT STATS SECTION #######
five_ot_stats_list   = [77,295,68,90,50,50,50,85,40,40,40,40,60,50,50,10,10]
five_ot_std_dev_list = [8,5,5,5,5,5,5,5,5,5,5,5,10,5,5,1,1]
ot_size = 15
five_ot_list = loop_stat_list(five_ot_stats_list, five_ot_std_dev_list, ot_size) 
#print(five_ot_list)
################################

####### OG,C STATS SECTION #######
five_og_stats_list   = [76,295,68,90,50,50,50,85,40,40,40,40,60,50,50,10,10]
five_og_std_dev_list = [6,4,5,5,5,5,5,5,5,5,5,5,10,5,5,1,1]
og_size = 10
c_size = 5
five_og_list = loop_stat_list(five_og_stats_list, five_te_std_dev_list, og_size) 
five_c_list = loop_stat_list(five_og_stats_list, five_og_std_dev_list, c_size)
#print(five_og_list)
#print(five_c_list)
################################

####### DT STATS SECTION #######
five_dt_stats_list   = [75,295,68,90,50,50,50,55,80,85,75,40,65,50,50,10,10]
five_dt_std_dev_list = [8,4,5,5,5,5,5,5,5,5,5,5,5,5,5,1,1]
dt_size = 15
five_dt_list = loop_stat_list(five_dt_stats_list, five_dt_std_dev_list, dt_size) 
#print(five_dt_list)
################################

####### EDGE STATS SECTION #######
five_edge_stats_list   = [75,275,80,80,50,50,50,55,85,80,80,60,65,50,50,10,10]
five_edge_std_dev_list = [6,4,10,5,5,5,5,5,5,5,5,5,5,5,5,1,1]
edge_size = 20
five_edge_list = loop_stat_list(five_edge_stats_list, five_edge_std_dev_list, edge_size) 
#print(five_edge_list)
################################

####### LB STATS SECTION #######
five_lb_stats_list   = [72,225,85,70,50,50,60,55,65,75,85,65,75,50,50,10,10]
five_lb_std_dev_list = [4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,1,1]
lb_size = 25
five_lb_list = loop_stat_list(five_lb_stats_list, five_lb_std_dev_list, lb_size) 
#print(five_lb_list)
################################

####### CB STATS SECTION #######
five_cb_stats_list   = [70,195,90,50,50,50,65,45,45,45,50,85,55,50,50,10,10]
five_cb_std_dev_list = [4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,1,1]
cb_size = 25
five_cb_list = loop_stat_list(five_cb_stats_list, five_cb_std_dev_list, cb_size) 
#print(five_cb_list)
################################

####### SAF STATS SECTION #######
five_saf_stats_list   = [70,205,90,65,50,50,65,45,55,65,75,75,75,50,50,10,10]
five_saf_std_dev_list = [4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,1,1]
saf_size = 25
five_saf_list = loop_stat_list(five_saf_stats_list, five_saf_std_dev_list, saf_size)
#print(five_saf_list)
################################
