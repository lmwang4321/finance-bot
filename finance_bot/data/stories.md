## story_001
* greet
   - utter_greet
* inform{"company": "Baidu"}
   - slot{"company": "Baidu"}
   - utter_ask_time
* inform{"time": "2018.2.1"}
   - slot{"time": "2018.2.1"}
   - utter_ask_info
* ask_open
   - action_open
* goodbye
   - utter_goodbye

## story_002
* greet
   - utter_greet
* inform{"company": "Google"}
   - slot{"company": "Google"}
   - utter_ask_time
* inform{"time": "2018.5.3"}
   - slot{"time": "2018.5.3"}
   - utter_ask_info
* ask_close
   - action_close
* goodbye
   - utter_goodbye


## story_003
* greet
   - utter_greet
* inform{"company": "Amazon"}
   - slot{"company": "Amazon"}
   - utter_ask_time
* inform{"time": "2018.7.2"}
   - slot{"time": "2018.7.2"}
   - utter_ask_info
* ask_volume
   - action_volume
* thanks
   - utter_goodbye


## story_004
* inform[company=Tencent]
   - slot{"company": "Tencent"}
   - utter_ask_time
* inform{"now": "at this time"}
   - action_current_price
* goodbye
   - utter_goodbye


## story_005
* inform{"company": "Facebook", "now": "current"}
   - slot{"company": "Facebook"}
   - slot{"now": "current"}
   - action_current_price
* thanks
   - utter_goodbye


## story_006
* greet
   - utter_greet
* inform[company=Priceline]
   - slot{"company": "Priceline"}
   - utter_ask_time
* inform{"time": "2018.5.13"}
   - slot{"time": "2018.5.13"}
   - utter_ask_info
* ask_peak
   - action_peak
* thanks
   - utter_goodbye


## story_007
* greet
   - utter_greet
* ask_open[company=Bilibili]
   - utter_ask_time
* inform{"time": "2018.6.13"}
   - slot{"time": "2018.6.13"}
   - action_open
* thanks
   - utter_goodbye


## story_007
* greet
   - utter_greet
* ask_close[company=Walmart]
   - utter_ask_time
* inform{"time": "2018.7.2"}
   - slot{"time": "2018.7.2"}
   - action_close
* thanks
   - utter_goodbye


## story_008
* greet
   - utter_greet
* ask_historical_plot[company=walmart, start_time=2018.2.1, end_time=2018.5.2]
   - slot{"company": "walmart"}
   - slot{"start_time": "2018.2.1"}
   - slot{"end_time": "2018.5.2"}
   - action_historical_plot
* goodbye
   - utter_goodbye

## story_009
* greet
   - utter_greet
* ask_historical_plot[company=apple, start_time=2018.5.3, end_time=2018.7.9]
   - slot{"company": "apple"}
   - slot{"start_time": "2018.5.3"}
   - slot{"end_time": "2018.7.9"}
   - action_historical_plot
* thanks
   - utter_goodbye

## story_010
* ask_historical_plot[company=NFLX, start_time=2017.11.1, end_time=2017.12.1]
   - slot{"company": "NFLX"}
   - slot{"start_time": "2017.11.1"}
   - slot{"end_time": "2017.12.1"}
   - action_historical_plot
* goodbye
   - utter_goodbye

## story_011
* ask_historical_plot[company=TGT, start_time=2017.10.1, end_time=2017.11.5]
   - slot{"company": "TGT"}
   - slot{"start_time": "2017.10.1"}
   - slot{"end_time": "2017.11.5"}
   - action_historical_plot
* thanks
   - utter_goodbye


## Generated Story -879327645589338
* greet
    - utter_greet
* goodbye
    - utter_goodbye
    - export

## Generated Story 1001767131690907919
* greet
    - utter_greet
* ask_historical_plot{"company": "googl", "start_time": "2018.3.2", "end_time": "2018.5.3"}
    - slot{"company": "googl"}
    - slot{"end_time": "2018.5.3"}
    - slot{"start_time": "2018.3.2"}
    - action_historical_plot
* goodbye
    - utter_goodbye
    - export

## Generated Story -3096389696659048674
* greet
    - utter_greet
* inform{"now": "current", "company": "baidu"}
    - slot{"company": "baidu"}
    - slot{"now": "current"}
    - action_current_price
    - slot{"company": "BIDU"}
* inform{"company": "baidu"}
    - slot{"company": "baidu"}
    - utter_ask_time
* inform{"time": "2018.5.3"}
    - slot{"time": "2018.5.3"}
    - utter_ask_info
* ask_open
    - action_open
    - slot{"company": "BIDU"}
    - slot{"time": "2018.5.3"}
* thanks
    - utter_goodbye
* inform{"company": "baidu"}
    - slot{"company": "baidu"}
    - utter_ask_time
* inform{"time": "2018.5.3"}
    - slot{"time": "2018.5.3"}
    - utter_ask_info
* ask_volume
    - action_volume
    - slot{"company": "BIDU"}
    - slot{"time": "2018.5.3"}
    - export

## Generated Story 1298956403919690286
* greet
    - utter_greet
* inform{"now": "current", "company": "alibaba"}
    - slot{"company": "alibaba"}
    - slot{"now": "current"}
    - action_current_price
    - slot{"company": "BABA"}
* inform{"company": "baidu"}
    - slot{"company": "baidu"}
    - utter_ask_time
* inform{"time": "2018.2.3"}
    - slot{"time": "2018.2.3"}
    - utter_ask_info
* ask_close
    - action_close
* thanks
    - utter_goodbye
    - export

## Generated Story 1622472457588234308
* greet
    - utter_greet
* inform{"now": "current", "company": "bilibili"}
    - slot{"company": "bilibili"}
    - slot{"now": "current"}
    - action_current_price
    - slot{"company": "BILI"}
* inform{"company": "blizzard"}
    - slot{"company": "blizzard"}
    - utter_ask_time
* inform{"time": "2018.2.5"}
    - slot{"time": "2018.2.5"}
    - utter_ask_info
* ask_volume
    - action_volume
    - slot{"company": "ATVI"}
    - slot{"time": "2018.2.5"}
* inform{"company": "alibaba"}
    - slot{"company": "alibaba"}
    - utter_ask_time
* inform{"time": "2017.12.1"}
    - slot{"time": "2017.12.1"}
    - utter_ask_info
* ask_open
    - action_open
    - slot{"company": "BABA"}
    - slot{"time": "2017.12.1"}
* thanks
    - utter_goodbye
* goodbye
    - utter_goodbye
    - export

## Generated Story 7782548020527572882
* greet
    - utter_greet
* inform{"company": "baidu"}
    - slot{"company": "baidu"}
    - utter_ask_time
* inform{"now": "right now"}
    - slot{"now": "right now"}
    - action_current_price
    - slot{"company": "BIDU"}
* inform{"now": "current", "company": "alibaba"}
    - slot{"company": "alibaba"}
    - slot{"now": "current"}
    - action_current_price
    - slot{"company": "BABA"}
* thanks
    - export

## Generated Story -6500711884172771656
* greet
    - utter_greet
* inform{"now": "current", "company": "baidu"}
    - slot{"company": "baidu"}
    - slot{"now": "current"}
    - action_current_price
* inform{"now": "current", "company": "alibaba"}
    - slot{"company": "alibaba"}
    - slot{"now": "current"}
    - action_current_price
* thanks
    - utter_goodbye
    - export

## Generated Story -1807825457029051580
* greet
    - utter_greet
* inform{"company": "baidu"}
    - slot{"company": "baidu"}
    - utter_ask_time
* inform{"time": "2018.5.3"}
    - slot{"time": "2018.5.3"}
    - utter_ask_info
* ask_volume
    - action_volume
    - slot{"company": "BIDU"}
    - slot{"time": "2018.5.3"}
* inform{"now": "current", "company": "alibaba"}
    - slot{"company": "alibaba"}
    - slot{"now": "current"}
    - action_current_price
    - slot{"company": "BABA"}
* thanks
    - utter_goodbye
    - export

