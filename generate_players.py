import numpy as np

#                  ht, wgt, sp, st, tp, ta, ct, bk, pr, bs, tk, cv, fq, bv, cy, kp, ka                
qb_rating_means = [72, 205, 75, 60, 85, 80, 30, 30, 30, 30, 30, 30, 75, 50, 50, 10, 10]
hb_rating_means = [68, 205, 88, 65, 30, 30, 65, 50, 30, 30, 30, 30, 60, 75, 75, 10, 10]
fb_rating_means = [70, 235, 70, 73, 50, 50, 65, 60, 50, 50, 50, 50, 60, 65, 65, 10, 10]
wr_rating_means = [70, 195, 88, 50, 30, 30, 75, 40, 30, 30, 30, 30, 60, 50, 60, 10, 10]
te_rating_means = [72, 225, 77, 70, 35, 30, 72, 60, 30, 30, 20, 30, 60, 60, 70, 10, 10]
ot_rating_means = [74, 295, 60, 85, 30, 30, 20, 77, 30, 30, 30, 30, 55, 50, 50, 10, 10]
og_rating_means = [72, 205, 75, 60, 85, 40, 50, 50, 50, 50, 50, 50, 75, 50, 50, 10, 10]
c_rating_means  = [72, 205, 75, 60, 85, 50, 50, 50, 50, 50, 50, 50, 75, 50, 50, 10, 10]
de_rating_means = [72, 205, 75, 60, 85, 50, 50, 50, 50, 50, 50, 50, 75, 50, 50, 10, 10]
dt_rating_means = [72, 205, 75, 60, 85, 50, 50, 50, 50, 50, 50, 50, 75, 50, 50, 10, 10]
lb_rating_means = [72, 205, 75, 60, 85, 50, 50, 50, 50, 50, 50, 50, 75, 50, 50, 10, 10]
cb_rating_means = [72, 205, 75, 60, 85, 50, 50, 50, 50, 50, 50, 50, 75, 50, 50, 10, 10]
s_rating_means  = [72, 205, 75, 60, 85, 50, 50, 50, 50, 50, 50, 50, 75, 50, 50, 10, 10]

def generate_stat_values(mean, std_dev, size):
    stats_values = np.random.normal(mean, std_dev, size)
    return stats_values

five_ot_hgt_values = generate_stat_values(77, 8, 15)
five_ot_wgt_values = generate_stat_values(295, 5, 15)
five_ot_spd_values = generate_stat_values(68, 5, 15)
five_ot_str_values = generate_stat_values(90, 5, 15)
five_ot_tpr_values = generate_stat_values(50, 5, 15)
five_ot_tha_values = generate_stat_values(50, 5, 15)
five_ot_cth_values = generate_stat_values(50, 5, 15)
five_ot_blk_values = generate_stat_values(85, 5, 15)
five_ot_prh_values = generate_stat_values(40, 5, 15)
five_ot_bks_values = generate_stat_values(40, 5, 15)
five_ot_tck_values = generate_stat_values(40, 5, 15)
five_ot_cov_values = generate_stat_values(40, 5, 15)
five_ot_fiq_values = generate_stat_values(60, 10, 15)
five_ot_bcv_values = generate_stat_values(50, 5, 15)
five_ot_cry_values = generate_stat_values(50, 5, 15)
five_ot_kpw_values = generate_stat_values(10, 5, 5)
five_ot_kac_values = generate_stat_values(10, 5, 5)

five_ot_list = [five_ot_hgt_values, five_ot_wgt_values, five_ot_spd_values, five_ot_str_values, 
                five_ot_tpr_values, five_ot_cth_values, five_ot_tha_values, five_ot_blk_values, 
                five_ot_prh_values, five_ot_bks_values, five_ot_tck_values, five_ot_cov_values,
                five_ot_fiq_values, five_ot_bcv_values, five_ot_cry_values, five_ot_kpw_values,
                five_ot_kac_values]
f_ot_final = np.array(five_ot_list)

print(f_ot_final)

five_og_hgt_values = generate_stat_values(76, 6, 10)
five_og_wgt_values = generate_stat_values(295, 4, 10)
five_og_spd_values = generate_stat_values(68, 5, 10)
five_og_str_values = generate_stat_values(90, 5, 10)
five_og_tpr_values = generate_stat_values(50, 5, 10)
five_og_tha_values = generate_stat_values(50, 5, 10)
five_og_cth_values = generate_stat_values(50, 5, 10)
five_og_blk_values = generate_stat_values(85, 5, 10)
five_og_prh_values = generate_stat_values(40, 5, 10)
five_og_bks_values = generate_stat_values(40, 5, 10)
five_og_tck_values = generate_stat_values(40, 5, 10)
five_og_cov_values = generate_stat_values(40, 5, 10)
five_og_fiq_values = generate_stat_values(60, 10, 10)
five_og_bcv_values = generate_stat_values(50, 5, 10)
five_og_cry_values = generate_stat_values(50, 5, 10)
five_og_kpw_values = generate_stat_values(10, 5, 5)
five_og_kac_values = generate_stat_values(10, 5, 5)

five_og_list = [five_og_hgt_values, five_og_wgt_values, five_og_spd_values, five_og_str_values, 
                five_og_tpr_values, five_og_cth_values, five_og_tha_values, five_og_blk_values, 
                five_og_prh_values, five_og_bks_values, five_og_tck_values, five_og_cov_values,
                five_og_fiq_values, five_og_bcv_values, five_og_cry_values, five_og_kpw_values,
                five_og_kac_values]
f_og_final = np.array(five_og_list)

print(f_og_final)

five_c_hgt_values = generate_stat_values(76, 6, 5)
five_c_wgt_values = generate_stat_values(295, 4, 5)
five_c_spd_values = generate_stat_values(68, 5, 5)
five_c_str_values = generate_stat_values(90, 5, 5)
five_c_tpr_values = generate_stat_values(50, 5, 5)
five_c_tha_values = generate_stat_values(50, 5, 5)
five_c_cth_values = generate_stat_values(50, 5, 5)
five_c_blk_values = generate_stat_values(85, 5, 5)
five_c_prh_values = generate_stat_values(40, 5, 5)
five_c_bks_values = generate_stat_values(40, 5, 5)
five_c_tck_values = generate_stat_values(40, 5, 5)
five_c_cov_values = generate_stat_values(40, 5, 5)
five_c_fiq_values = generate_stat_values(60, 10, 5)
five_c_bcv_values = generate_stat_values(50, 5, 5)
five_c_cry_values = generate_stat_values(50, 5, 5)
five_c_kpw_values = generate_stat_values(10, 5, 5)
five_c_kac_values = generate_stat_values(10, 5, 5)

five_c_list = [five_c_hgt_values, five_c_wgt_values, five_c_spd_values, five_c_str_values, 
                five_c_tpr_values, five_c_cth_values, five_c_tha_values, five_c_blk_values, 
                five_c_prh_values, five_c_bks_values, five_c_tck_values, five_c_cov_values,
                five_c_fiq_values, five_c_bcv_values, five_c_cry_values, five_c_kpw_values,
                five_c_kac_values]
f_c_final = np.array(five_c_list)

print(f_c_final)

five_dt_hgt_values = generate_stat_values(75, 6, 5)
five_dt_wgt_values = generate_stat_values(295, 4, 5)
five_dt_spd_values = generate_stat_values(68, 5, 5)
five_dt_str_values = generate_stat_values(90, 5, 5)
five_dt_tpr_values = generate_stat_values(50, 5, 5)
five_dt_tha_values = generate_stat_values(50, 5, 5)
five_dt_cth_values = generate_stat_values(50, 5, 5)
five_dt_blk_values = generate_stat_values(55, 5, 5)
five_dt_prh_values = generate_stat_values(80, 5, 5)
five_dt_bks_values = generate_stat_values(85, 5, 5)
five_dt_tck_values = generate_stat_values(75, 5, 5)
five_dt_cov_values = generate_stat_values(40, 5, 5)
five_dt_fiq_values = generate_stat_values(65, 5, 5)
five_dt_bcv_values = generate_stat_values(50, 5, 5)
five_dt_cry_values = generate_stat_values(50, 5, 5)
five_dt_kpw_values = generate_stat_values(10, 5, 5)
five_dt_kac_values = generate_stat_values(10, 5, 5)

five_dt_list = [five_dt_hgt_values, five_dt_wgt_values, five_dt_spd_values, five_dt_str_values, 
                five_dt_tpr_values, five_dt_cth_values, five_dt_tha_values, five_dt_blk_values, 
                five_dt_prh_values, five_dt_bks_values, five_dt_tck_values, five_dt_cov_values,
                five_dt_fiq_values, five_dt_bcv_values, five_dt_cry_values, five_dt_kpw_values,
                five_dt_kac_values]
f_dt_final = np.array(five_dt_list)

print(f_dt_final)

five_edge_hgt_values = generate_stat_values(75, 6, 5)
five_edge_wgt_values = generate_stat_values(295, 4, 5)
five_edge_spd_values = generate_stat_values(80, 10, 5)
five_edge_str_values = generate_stat_values(80, 5, 5)
five_edge_tpr_values = generate_stat_values(50, 5, 5)
five_edge_tha_values = generate_stat_values(50, 5, 5)
five_edge_cth_values = generate_stat_values(50, 5, 5)
five_edge_blk_values = generate_stat_values(55, 5, 5)
five_edge_prh_values = generate_stat_values(85, 5, 5)
five_edge_bks_values = generate_stat_values(80, 5, 5)
five_edge_tck_values = generate_stat_values(80, 5, 5)
five_edge_cov_values = generate_stat_values(60, 5, 5)
five_edge_fiq_values = generate_stat_values(65, 5, 5)
five_edge_bcv_values = generate_stat_values(50, 5, 5)
five_edge_cry_values = generate_stat_values(50, 5, 5)
five_edge_kpw_values = generate_stat_values(10, 5, 5)
five_edge_kac_values = generate_stat_values(10, 5, 5)

five_edge_list = [five_edge_hgt_values, five_edge_wgt_values, five_edge_spd_values, five_edge_str_values, 
                five_edge_tpr_values, five_edge_cth_values, five_edge_tha_values, five_edge_blk_values, 
                five_edge_prh_values, five_edge_bks_values, five_edge_tck_values, five_edge_cov_values,
                five_edge_fiq_values, five_edge_bcv_values, five_edge_cry_values, five_edge_kpw_values,
                five_edge_kac_values]
f_edge_final = np.array(five_edge_list)

print(f_edge_final)

five_lb_hgt_values = generate_stat_values(72, 4, 5)
five_lb_wgt_values = generate_stat_values(225, 4, 5)
five_lb_spd_values = generate_stat_values(85, 5, 5)
five_lb_str_values = generate_stat_values(70, 5, 5)
five_lb_tpr_values = generate_stat_values(50, 5, 5)
five_lb_tha_values = generate_stat_values(50, 5, 5)
five_lb_cth_values = generate_stat_values(60, 5, 5)
five_lb_blk_values = generate_stat_values(55, 5, 5)
five_lb_prh_values = generate_stat_values(65, 5, 5)
five_lb_bks_values = generate_stat_values(75, 5, 5)
five_lb_tck_values = generate_stat_values(85, 5, 5)
five_lb_cov_values = generate_stat_values(65, 5, 5)
five_lb_fiq_values = generate_stat_values(75, 5, 5)
five_lb_bcv_values = generate_stat_values(50, 5, 5)
five_lb_cry_values = generate_stat_values(50, 5, 5)

five_lb_list = [five_lb_hgt_values, five_lb_wgt_values, five_lb_spd_values, five_lb_str_values, 
                five_lb_tpr_values, five_lb_cth_values, five_lb_tha_values, five_lb_blk_values, 
                five_lb_prh_values, five_lb_bks_values, five_lb_tck_values, five_lb_cov_values,
                five_lb_fiq_values, five_lb_bcv_values, five_lb_cry_values]
f_lb_final = np.array(five_lb_list)

print(f_lb_final)

five_cb_hgt_values = generate_stat_values(70, 4, 5)
five_cb_wgt_values = generate_stat_values(195, 4, 5)
five_cb_spd_values = generate_stat_values(90, 5, 5)
five_cb_str_values = generate_stat_values(50, 5, 5)
five_cb_tpr_values = generate_stat_values(50, 5, 5)
five_cb_tha_values = generate_stat_values(50, 5, 5)
five_cb_cth_values = generate_stat_values(65, 5, 5)
five_cb_blk_values = generate_stat_values(45, 5, 5)
five_cb_prh_values = generate_stat_values(45, 5, 5)
five_cb_bks_values = generate_stat_values(45, 5, 5)
five_cb_tck_values = generate_stat_values(60, 5, 5)
five_cb_cov_values = generate_stat_values(85, 5, 5)
five_cb_fiq_values = generate_stat_values(65, 5, 5)
five_cb_bcv_values = generate_stat_values(50, 5, 5)
five_cb_cry_values = generate_stat_values(50, 5, 5)
five_cb_kpw_values = generate_stat_values(10, 5, 5)
five_cb_kac_values = generate_stat_values(10, 5, 5)

five_cb_list = [five_cb_hgt_values, five_cb_wgt_values, five_cb_spd_values, five_cb_str_values, 
                five_cb_tpr_values, five_cb_cth_values, five_cb_tha_values, five_cb_blk_values, 
                five_cb_prh_values, five_cb_bks_values, five_cb_tck_values, five_cb_cov_values,
                five_cb_fiq_values, five_cb_bcv_values, five_cb_cry_values, five_cb_kpw_values,
                five_cb_kac_values]
f_cb_final = np.array(five_cb_list)

print(f_cb_final)

five_saf_hgt_values = generate_stat_values(70, 4, 5)
five_saf_wgt_values = generate_stat_values(205, 4, 5)
five_saf_spd_values = generate_stat_values(90, 5, 5)
five_saf_str_values = generate_stat_values(65, 5, 5)
five_saf_tpr_values = generate_stat_values(50, 5, 5)
five_saf_tha_values = generate_stat_values(50, 5, 5)
five_saf_cth_values = generate_stat_values(65, 5, 5)
five_saf_blk_values = generate_stat_values(45, 5, 5)
five_saf_prh_values = generate_stat_values(55, 5, 5)
five_saf_bks_values = generate_stat_values(65, 5, 5)
five_saf_tck_values = generate_stat_values(75, 5, 5)
five_saf_cov_values = generate_stat_values(75, 5, 5)
five_saf_fiq_values = generate_stat_values(75, 5, 5)
five_saf_bcv_values = generate_stat_values(50, 5, 5)
five_saf_cry_values = generate_stat_values(50, 5, 5)
five_saf_kpw_values = generate_stat_values(10, 5, 5)
five_saf_kac_values = generate_stat_values(10, 5, 5)

five_saf_list = [five_saf_hgt_values, five_saf_wgt_values, five_saf_spd_values, five_saf_str_values, 
                five_saf_tpr_values, five_saf_cth_values, five_saf_tha_values, five_saf_blk_values, 
                five_saf_prh_values, five_saf_bks_values, five_saf_tck_values, five_saf_cov_values,
                five_saf_fiq_values, five_saf_bcv_values, five_saf_cry_values, five_saf_kpw_values,
                five_saf_kac_values]
f_saf_final = np.array(five_saf_list)

