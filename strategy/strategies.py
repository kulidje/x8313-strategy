from horse.betsim.strategy.factors import between, isin, merge_dicts

# test strategy: ml_rank2_85_92 using post cols
ml_rank2_85_92_v1 = merge_dicts(
                                between('entropy_prob_morning_line_pre', 0.85, 0.92),
                                between('num_starters_pre', 8, 8),
                                between('rank_prob_morning_line_pre', 2, 2)
                               )

# test strategy: ml_rank2_85_92 using post cols
ml_rank2_85_92_v2 = merge_dicts(
                                between('entropy_prob_morning_line_post', 0.85, 0.92),
                                between('num_starters_post', 8, 8),
                                between('rank_prob_morning_line_post', 2, 2),
                                isin('race_race_type', ['G1', 'G2', 'G3', 'N'])
                               )

ML8592R2_V01 = merge_dicts(
                            between('entropy_prob_morning_line_post', 0.85, 0.92),
                            between('num_starters_post', 8, 8),
                            between('rank_prob_morning_line_post', 2, 2),
                               )

SPPK_WIN = merge_dicts(
                       isin('race_surface', ['D']),
                       between('num_starters_post', 6, 6),
                       isin('race_race_type', ['C']),
                       between('rank_hdw_sppk', 1, 1),
                       between('rank_ml_sppk', 3, 6),
                       isin('is_T4_h4_9166', [True]),
                       isin('coupled_race', [False]),
                      )

# this is geared to old system (See betting.py)
SPPK_WIN_mini = merge_dicts(
                            between('num_starters_0', 6, 6),  # num starters pre
                            between('rank_hdw_sppk_0', 1, 1),
                            between('rank_ml_sppk_0', 3, 6),
                            isin('idxT4_prob_runner_HDWPSRRating_0', ['h4_9166'])
                            )

p4_hdw_top4 = merge_dicts(
                          between('rank_hdw_sppk_0', 1, 4),
                          between('rank_hdw_sppk_1', 1, 4),
                          between('rank_hdw_sppk_2', 1, 4),
                          between('rank_hdw_sppk_3', 1, 4)
                         )

houston = merge_dicts(
                      between('rank_hdw_sppk_0', 1, 1),
                      between('x8runner_HDWPSRRating_norm_par_0', 1, 100),
                      )

TESTFAVR_V01 = merge_dicts(
                            between('rank_prob_morning_line_post', 1, 1),
                               )


iv_stakes_1_1_1_1_v2 = merge_dicts(isin('race_race_type', ['G1', 'G2', 'G3', 'N']),
                                   between('num_iv_score_total_3', 1, 1),
                                   between('iv_score_jockey', 1, 1),
                                   between('iv_score_trainer', 1, 1),
                                   between('iv_score_median_runner_HDWPSRRating', 1, 1),
                                   between('rank_prob_morning_line_post', 2, 5))

iv_stakes_0_1_0_0_v2 = merge_dicts(isin('race_race_type', ['G1', 'G2', 'G3', 'N']),
                                   between('num_iv_score_total_3', 0, 0),
                                   between('iv_score_jockey', 1, 1),
                                   between('iv_score_trainer', 0, 0),
                                   between('iv_score_median_runner_HDWPSRRating', 0, 0),
                                   between('rank_prob_morning_line_post', 2, 5))

# testing betting this on Fridays for 2019 summer, stopped doing this late Oct. 2019
iv_stakes_0_1_0_0 = merge_dicts(isin('race_race_type_0', ['G1', 'G2', 'G3', 'N']),
                                between('num_iv_score_total_3_0', 0, 0),
                                between('iv_score_jockey_0', 1, 1),
                                between('iv_score_trainer_0', 0, 0),
                                between('iv_score_median_runner_HDWPSRRating_0', 0, 0),
                                between('rank_morning_line_0', 2, 5))

# TODO normalize between all generating functions. columns are configured to consume_betting_trigger.py, not Simulator()
Muchacho_V01 = merge_dicts(
    between('entropy_prob_morning_line_post', 0.85, 0.92),
    between('num_starters_post', 8, 8),
    between('rank_prob_morning_line_post', 2, 2),
    isin('coupled_race', [False]),
    isin('race_race_type', ['G1', 'G2', 'G3', 'N'])

)


# def cond_WN_2F(pipe):
#     strategy = 'cond_WN_2F'
#     # IMPORTANT - target_races must be list of unique race_id's (no duplicates)
#     # has_rebate = pipe.dr.dftrack[pipe.dr.dftrack.WN.fillna(0) > 0].itsp_track_sym
#     target_races = pipe.dr.dfX.race_id.unique()
#     for race_id in target_races:
#
#         # if we're working inside the race for loop, we can assume that pipe.df_bets is only 1 race
#         # pipe.run() must be first line in the race for loop
#         pipe.run(race_id, 'WN')
#
#         # filter: num_runners with score of 3 == 0 is equivalent to Zero contenders from x8raceclass
#         pipe.df_bets = pipe.df_bets[pipe.df_bets['num_iv_score_total_3'] ==0] # Only races with zero contenders
#         pipe.df_bets = pipe.df_bets[ (pipe.df_bets['iv_score_total_0']==2) & (pipe.df_bets['iv_score_jockey_0']==1)]
#         pipe.df_bets = pipe.df_bets[pipe.df_bets['factor_gts_0'].isin(['win'])]
#
#         # $10 each
#         pipe.df_bets['bet_amount'] = 10
#
#     # format bets rounds up using math.ceil()
#     pipe.format_bets(strategy)
#     return pipe
#
#
# def cond_WN_2F_GTS(pipe):
#     # TODO test __name__
#     strategy = 'cond_WN_2F_GTS'
#     # IMPORTANT - target_races must be list of unique race_id's (no duplicates)
#     # has_rebate = pipe.dr.dftrack[pipe.dr.dftrack.WN.fillna(0) > 0].itsp_track_sym
#     target_races = pipe.dr.dfX.race_id.unique()
#     for race_id in target_races:
#         # if we're working inside the race for loop, we can assume that pipe.df_bets is only 1 race
#         # pipe.run() must be first line in the race for loop
#         pipe.run(race_id, 'WN')
#         # filter: num_runners with score of 3 == 0 is equivalent to Zero contenders from x8raceclass
#         pipe.df_bets = pipe.df_bets[pipe.df_bets['num_iv_score_total_3'] ==0] # Only races with zero contenders
#         pipe.df_bets = pipe.df_bets[ (pipe.df_bets['iv_score_total_0']==2) & (pipe.df_bets['iv_score_jockey_0']==1)]
#         pipe.df_bets = pipe.df_bets[pipe.df_bets['factor_gts_0'].isin(['win', 'place', 'show', 'wildcard', 'a1', 'a2'])]
#         # $2 each (this has been tampered with a little)
#         pipe.df_bets['bet_amount'] = 2
#     # format bets rounds up using math.ceil()
#     pipe.format_bets(strategy)
#     return pipe
#
#
# def score3_1runner(pipe):
#     strategy = 'score3_1runner'
#     # IMPORTANT - target_races must be list of unique race_id's (no duplicates)
#     has_rebate = pipe.dr.dftrack[pipe.dr.dftrack.WN.fillna(0) > 0].itsp_track_sym
#     target_races = pipe.dr.dfX[pipe.dr.dfX['itsp_track_sym'].isin(has_rebate)].race_id.unique()
#     for race_id in target_races:
#         # if we're working inside the race for loop, we can assume that df_bets is only 1 race (important for race_risk)
#         # pipe.run() must be first line in the race for loop
#         pipe.run(race_id, 'WN')
#         # filter: score of 3
#         pipe.df_bets = pipe.df_bets[pipe.df_bets['iv_score_total_0'] > 2]
#         # $10 each
#         pipe.df_bets['bet_amount'] = 10
#         # filter: only bet races where there is one runner with score of 3
#         pipe.df_bets['race_risk'] = pipe.df_bets['bet_amount'].sum()
#         pipe.df_bets = pipe.df_bets[pipe.df_bets['race_risk'] == 10]
#     pipe.format_bets(strategy)
#     return pipe
#
#
# def score3_ml_WN(pipe):
#     strategy = 'score3_ml_WN'
#
#     # IMPORTANT - target_races must be list of unique race_id's (no duplicates)
#     has_rebate = pipe.dr.dftrack[pipe.dr.dftrack.WN.fillna(0) > 0].itsp_track_sym
#     target_races = pipe.dr.dfX[pipe.dr.dfX['itsp_track_sym'].isin(has_rebate)].race_id.unique()
#
#     for race_id in target_races:
#         # if we're working inside the race for loop, we can assume that pipe.df_bets is only 1 race
#         # pipe.run() must be first line in the race for loop
#         pipe.run(race_id, 'WN')
#
#         # filter: score of 3
#         pipe.df_bets = pipe.df_bets[pipe.df_bets['iv_score_total_0'] > 2]
#
#         target_runners = pipe.df_bets.index
#
#         # this assigns a column named: harville_{prob_model} to pipe.df_bets
#         pipe.calibrate(prob_model='prob_morning_line', runners=target_runners)
#
#         # risk part
#         pipe.df_bets['bet_amount'] = pipe.df_bets['harville_prob_morning_line'].values * 10
#
#         # filter: bet_amount not null() i.e. runners was not targeted
#         pipe.df_bets = pipe.df_bets[pipe.df_bets['bet_amount'].notnull()]
#     # format bets rounds up using math.ceil()
#     pipe.format_bets(strategy)
#
#     return pipe
#
# def score3_ml_EX(pipe):
#     strategy = 'score3_ml_EX'
#
#     # IMPORTANT - target_races must be list of unique race_id's (no duplicates)
#     has_rebate = pipe.dr.dftrack[pipe.dr.dftrack.WN.fillna(0) > 0].itsp_track_sym
#     target_races = pipe.dr.dfX[pipe.dr.dfX['itsp_track_sym'].isin(has_rebate)].race_id.unique()
#     for race_id in target_races:
#         # if we're working inside the race for loop, we can assume that pipe.df_bets is only 1 race
#         # pipe.run() must be first line in the race for loop
#         pipe.run(race_id, 'EX')
#
#         # filter: score of 3
#         pipe.df_bets = pipe.df_bets[pipe.df_bets['iv_score_total_0'] > 2]
#         pipe.df_bets = pipe.df_bets[pipe.df_bets['iv_score_total_1'] > 2]
#
#         target_runners = pipe.df_bets.index.get_level_values(0)
#
#         # this assigns a column named: harville_{prob_model} to pipe.df_bets
#         pipe.calibrate(prob_model='prob_morning_line', runners=target_runners)
#
#         # risk part
#         pipe.df_bets['bet_amount'] = pipe.df_bets['harville_prob_morning_line'].values * 10
#
#         # filter: bet_amount not null() i.e. runners was not targeted
#         pipe.df_bets = pipe.df_bets[pipe.df_bets['bet_amount'].notnull()]
#
#     # format bets rounds up using math.ceil()
#     pipe.format_bets(strategy)
#
#     return pipe
#
#
# def score2_ml_WN(pipe):
#     strategy = 'score2_ml_WN'
#
#     # IMPORTANT - target_races must be list of unique race_id's (no duplicates)
#     has_rebate = pipe.dr.dftrack[pipe.dr.dftrack.WN.fillna(0) > 0].itsp_track_sym
#     target_races = pipe.dr.dfX[pipe.dr.dfX['itsp_track_sym'].isin(has_rebate)].race_id.unique()
#
#     for race_id in target_races:
#         # if we're working inside the race for loop, we can assume that pipe.df_bets is only 1 race
#         # pipe.run() must be first line in the race for loop
#         pipe.run(race_id, 'WN')
#
#         # filter: score of 3
#         pipe.df_bets = pipe.df_bets[pipe.df_bets['iv_score_total_0'] == 2]
#
#         target_runners = pipe.df_bets.index
#
#         # this assigns a column named: harville_{prob_model} to pipe.df_bets
#         pipe.calibrate(prob_model='prob_morning_line', runners=target_runners)
#
#         # risk part
#         pipe.df_bets['bet_amount'] = pipe.df_bets['harville_prob_morning_line'].values * 10
#
#         # filter: bet_amount not null() i.e. runners was not targeted
#         pipe.df_bets = pipe.df_bets[pipe.df_bets['bet_amount'].notnull()]
#
#     # format bets rounds up using math.ceil()
#     pipe.format_bets(strategy)
#
#     return pipe
#
#
# def score2_ml_EX(pipe):
#     strategy = 'score2_ml_EX'
#
#     # IMPORTANT - target_races must be list of unique race_id's (no duplicates)
#     has_rebate = pipe.dr.dftrack[pipe.dr.dftrack.WN.fillna(0) > 0].itsp_track_sym
#     target_races = pipe.dr.dfX[pipe.dr.dfX['itsp_track_sym'].isin(has_rebate)].race_id.unique()
#
#     for race_id in target_races:
#         # if we're working inside the race for loop, we can assume that pipe.df_bets is only 1 race
#         # pipe.run() must be first line in the race for loop
#         pipe.run(race_id, 'EX')
#
#         # filter: score of 3
#         pipe.df_bets = pipe.df_bets[pipe.df_bets['iv_score_total_0'] == 2]
#         pipe.df_bets = pipe.df_bets[pipe.df_bets['iv_score_total_1'] == 2]
#
#         target_runners = pipe.df_bets.index.get_level_values(0)
#
#         # this assigns a column named: harville_{prob_model} to pipe.df_bets
#         pipe.calibrate(prob_model='prob_morning_line', runners=target_runners)
#
#         # risk part
#         pipe.df_bets['bet_amount'] = pipe.df_bets['harville_prob_morning_line'].values * 10
#
#         # filter: bet_amount not null() i.e. runners was not targeted
#         pipe.df_bets = pipe.df_bets[pipe.df_bets['bet_amount'].notnull()]
#
#     # format bets rounds up using math.ceil()
#     pipe.format_bets(strategy)
#
#     return pipe
#
#
# def score12_EX(pipe):
#     strategy = 'score12_EX'
#     # IMPORTANT - target_races must be list of unique race_id's (no duplicates)
#     has_rebate = pipe.dr.dftrack[pipe.dr.dftrack.WN.fillna(0) > 0].itsp_track_sym
#     target_races = pipe.dr.dfX[pipe.dr.dfX['itsp_track_sym'].isin(has_rebate)].race_id.unique()
#     for race_id in target_races:
#         # if we're working inside the race for loop, we can assume that pipe.df_bets is only 1 race
#         # pipe.run() must be first line in the race for loop
#         pipe.run(race_id, 'EX')
#         # filter: score
#         pipe.df_bets = pipe.df_bets[pipe.df_bets['iv_score_total_0'] == 1]
#         pipe.df_bets = pipe.df_bets[pipe.df_bets['iv_score_total_1'] == 2]
#
#     # format bets rounds up using math.ceil()
#     pipe.format_bets(strategy)
#     return pipe
#
#
# def universe_EX(pipe):
#     strategy = 'universe_EX'
#     target_races = pipe.dr.dfX.race_id.unique()
#     for race_id in target_races:
#         pipe.run(race_id, 'EX')
#     pipe.format_bets(strategy)
#     return pipe
#
#
# def universe_TR(pipe):
#     strategy = 'universe_TR'
#     target_races = pipe.dr.dfX.race_id.unique()
#     for race_id in target_races:
#         pipe.run(race_id, 'TR')
#     pipe.format_bets(strategy)
#     return pipe
#
#
# def universe_WN(pipe):
#     strategy = 'universe_WN'
#     target_races = pipe.dr.dfX.race_id.unique()
#     for race_id in target_races:
#         pipe.run(race_id, 'WN')
#     pipe.format_bets(strategy)
#     return pipe
#
#
# def universe_PL(pipe):
#     strategy = 'universe_PL'
#     target_races = pipe.dr.dfX.race_id.unique()
#     for race_id in target_races:
#         pipe.run(race_id, 'PL')
#     pipe.format_bets(strategy)
#     return pipe
#
#
# def universe_SH(pipe):
#     strategy = 'universe_SH'
#     target_races = pipe.dr.dfX.race_id.unique()
#     for race_id in target_races:
#         pipe.run(race_id, 'SH')
#     pipe.format_bets(strategy)
#     return pipe
#
#
# def universe_SU(pipe):
#     strategy = 'universe_SU'
#     target_races = pipe.dr.dfX.race_id.unique()
#     for race_id in target_races:
#         pipe.run(race_id, 'SU')
#     pipe.format_bets(strategy)
#     return pipe
#
#
# def iv_stakes_1_1_1_1(pipe):
#     strategy = 'iv_stakes_1_1_1_1'
#     target_races = pipe.dr.dfX[pipe.dr.dfX['race_race_type'].isin(['G1', 'G2', 'G3', 'N'])].race_id.unique()
#     for race_id in target_races:
#         # if we're working inside the race for loop, we can assume that df_bets is only 1 race (important for race_risk)
#         # pipe.run() must be first line in the race for loop
#         pipe.run(race_id, 'WN')
#
#         # filter
#         pipe.df_bets = pipe.df_bets[pipe.df_bets['num_iv_score_total_3'] == 1]
#         pipe.df_bets = pipe.df_bets[pipe.df_bets['iv_score_jockey_0'] == 1]
#         pipe.df_bets = pipe.df_bets[pipe.df_bets['iv_score_trainer_0'] == 1]
#         pipe.df_bets = pipe.df_bets[pipe.df_bets['iv_score_median_runner_HDWPSRRating_0'] == 1]
#         pipe.df_bets = pipe.df_bets[pipe.df_bets['rank_morning_line_0'].between(2, 5)]
#
#         # $5 each
#         pipe.df_bets['bet_amount'] = 5
#
#     pipe.format_bets(strategy)
#
#     return pipe
#
#
# def iv_stakes_0_1_0_0(pipe):
#     strategy = 'iv_stakes_0_1_0_0'
#     target_races = pipe.dr.dfX[pipe.dr.dfX['race_race_type'].isin(['G1', 'G2', 'G3', 'N'])].race_id.unique()
#     for race_id in target_races:
#         # if we're working inside the race for loop, we can assume that df_bets is only 1 race (important for race_risk)
#         # pipe.run() must be first line in the race for loop
#         pipe.run(race_id, 'WN')
#
#         # filter
#         pipe.df_bets = pipe.df_bets[pipe.df_bets['num_iv_score_total_3'] == 0]
#         pipe.df_bets = pipe.df_bets[pipe.df_bets['iv_score_jockey_0'] == 1]
#         pipe.df_bets = pipe.df_bets[pipe.df_bets['iv_score_trainer_0'] == 0]
#         pipe.df_bets = pipe.df_bets[pipe.df_bets['iv_score_median_runner_HDWPSRRating_0'] == 0]
#         pipe.df_bets = pipe.df_bets[pipe.df_bets['rank_morning_line_0'].between(2, 5)]
#
#         # $2 each
#         pipe.df_bets['bet_amount'] = 2
#
#     pipe.format_bets(strategy)
#
#     return pipe
