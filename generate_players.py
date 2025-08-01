import numpy as np

def generate_stat_values(mean, std_dev, size):
    stats_values = np.random.normal(mean, std_dev, size)
    return stats_values

five_qb_hgt_values = generate_stat_values(74, 5, 5)
five_qb_wgt_values = generate_stat_values(205, 5, 5)
five_qb_spd_values = generate_stat_values(83, 5, 5)
five_qb_str_values = generate_stat_values(60, 5, 5)
five_qb_tpr_values = generate_stat_values(90, 5, 5)
five_qb_tha_values = generate_stat_values(85, 10, 5)
five_qb_cth_values = generate_stat_values(50, 5, 5)
five_qb_blk_values = generate_stat_values(50, 5, 5)
five_qb_prh_values = generate_stat_values(50, 5, 5)
five_qb_bks_values = generate_stat_values(50, 5, 5)
five_qb_tck_values = generate_stat_values(50, 5, 5)
five_qb_cov_values = generate_stat_values(50, 5, 5)
five_qb_fiq_values = generate_stat_values(75, 10, 5)
five_qb_bcv_values = generate_stat_values(50, 5, 5)
five_qb_cry_values = generate_stat_values(50, 5, 5)
five_qb_kpw_values = generate_stat_values(10, 5, 5)
five_qb_kac_values = generate_stat_values(10, 5, 5)

five_qb_list = [five_qb_hgt_values, five_qb_wgt_values, five_qb_spd_values, five_qb_str_values, 
                five_qb_tpr_values, five_qb_cth_values, five_qb_tha_values, five_qb_blk_values, 
                five_qb_prh_values, five_qb_bks_values, five_qb_tck_values, five_qb_cov_values,
                five_qb_fiq_values, five_qb_bcv_values, five_qb_cry_values, five_qb_kpw_values,
                five_qb_kac_values]
f_qb_final = np.array(five_qb_list)

print(f_qb_final)

five_hb_hgt_values = generate_stat_values(71, 5, 10)
five_hb_wgt_values = generate_stat_values(205, 5, 10)
five_hb_spd_values = generate_stat_values(92, 5, 10)
five_hb_str_values = generate_stat_values(65, 8, 10)
five_hb_tpr_values = generate_stat_values(50, 5, 10)
five_hb_tha_values = generate_stat_values(50, 5, 10)
five_hb_cth_values = generate_stat_values(70, 5, 10)
five_hb_blk_values = generate_stat_values(60, 5, 10)
five_hb_prh_values = generate_stat_values(50, 5, 10)
five_hb_bks_values = generate_stat_values(50, 5, 10)
five_hb_tck_values = generate_stat_values(50, 5, 10)
five_hb_cov_values = generate_stat_values(50, 5, 10)
five_hb_fiq_values = generate_stat_values(60, 10, 10)
five_hb_bcv_values = generate_stat_values(80, 10, 10)
five_hb_cry_values = generate_stat_values(80, 10, 10)
five_hb_kpw_values = generate_stat_values(10, 5, 5)
five_hb_kac_values = generate_stat_values(10, 5, 5)

five_hb_list = [five_hb_hgt_values, five_hb_wgt_values, five_hb_spd_values, five_hb_str_values, 
                five_hb_tpr_values, five_hb_cth_values, five_hb_tha_values, five_hb_blk_values, 
                five_hb_prh_values, five_hb_bks_values, five_hb_tck_values, five_hb_cov_values,
                five_hb_fiq_values, five_hb_bcv_values, five_hb_cry_values, five_hb_kpw_values,
                five_hb_kac_values]
f_hb_final = np.array(five_hb_list)

print(f_hb_final)

five_wr_hgt_values = generate_stat_values(70, 8, 20)
five_wr_wgt_values = generate_stat_values(205, 5, 20)
five_wr_spd_values = generate_stat_values(92, 5, 20)
five_wr_str_values = generate_stat_values(60, 5, 20)
five_wr_tpr_values = generate_stat_values(50, 5, 20)
five_wr_tha_values = generate_stat_values(50, 5, 20)
five_wr_cth_values = generate_stat_values(85, 5, 20)
five_wr_blk_values = generate_stat_values(50, 5, 20)
five_wr_prh_values = generate_stat_values(40, 5, 20)
five_wr_bks_values = generate_stat_values(40, 5, 20)
five_wr_tck_values = generate_stat_values(40, 5, 20)
five_wr_cov_values = generate_stat_values(40, 5, 20)
five_wr_fiq_values = generate_stat_values(60, 10, 20)
five_wr_bcv_values = generate_stat_values(70, 8, 20)
five_wr_cry_values = generate_stat_values(70, 8, 20)
five_wr_kpw_values = generate_stat_values(10, 5, 5)
five_wr_kac_values = generate_stat_values(10, 5, 5)

five_wr_list = [five_wr_hgt_values, five_wr_wgt_values, five_wr_spd_values, five_wr_str_values, 
                five_wr_tpr_values, five_wr_cth_values, five_wr_tha_values, five_wr_blk_values, 
                five_wr_prh_values, five_wr_bks_values, five_wr_tck_values, five_wr_cov_values,
                five_wr_fiq_values, five_wr_bcv_values, five_wr_cry_values, five_wr_kpw_values,
                five_wr_kac_values]
f_wr_final = np.array(five_wr_list)

print(f_wr_final)

five_te_hgt_values = generate_stat_values(76, 8, 8)
five_te_wgt_values = generate_stat_values(245, 5, 8)
five_te_spd_values = generate_stat_values(87, 5, 8)
five_te_str_values = generate_stat_values(70, 5, 8)
five_te_tpr_values = generate_stat_values(50, 5, 8)
five_te_tha_values = generate_stat_values(50, 5, 8)
five_te_cth_values = generate_stat_values(83, 5, 8)
five_te_blk_values = generate_stat_values(65, 5, 8)
five_te_prh_values = generate_stat_values(40, 5, 8)
five_te_bks_values = generate_stat_values(40, 5, 8)
five_te_tck_values = generate_stat_values(40, 5, 8)
five_te_cov_values = generate_stat_values(40, 5, 8)
five_te_fiq_values = generate_stat_values(60, 10, 8)
five_te_bcv_values = generate_stat_values(60, 5, 8)
five_te_cry_values = generate_stat_values(60, 5, 8)
five_te_kpw_values = generate_stat_values(10, 5, 5)
five_te_kac_values = generate_stat_values(10, 5, 5)

five_te_list = [five_te_hgt_values, five_te_wgt_values, five_te_spd_values, five_te_str_values, 
                five_te_tpr_values, five_te_cth_values, five_te_tha_values, five_te_blk_values, 
                five_te_prh_values, five_te_bks_values, five_te_tck_values, five_te_cov_values,
                five_te_fiq_values, five_te_bcv_values, five_te_cry_values, five_te_kpw_values,
                five_te_kac_values]
f_te_final = np.array(five_te_list)

print(f_te_final)

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

