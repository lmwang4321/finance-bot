## story_001
* greet
   - utter_greet
* ask_price[company=BIDU]
   - slot{"company": "BIDU"}
   - action_price
* goodbye
   - utter_goodbye

## story_002
* greet
   - utter_greet
* ask_price[company=GOOGL]
   - slot{"company": "GOOGL"}
   - action_price
* goodbye
   - utter_goodbye

## story_003
* greet
   - utter_greet
* ask_price[company=BILI]
   - slot{"company": "BILI"}
   - action_price
* goodbye
   - utter_goodbye

## story_004
* ask_price[company=TSLA]
   - slot{"company": "TSLA"}
   - action_price
* goodbye
   - utter_goodbye

## story_005
* ask_price[company=AMZN]
   - slot{"company": "AMZN"}
   - action_price

## story_006
* greet
   - utter_greet
* ask_price[company=PCLN]
   - slot{"company": "PCLN"}
   - action_price
* goodbye
   - utter_goodbye

## story_007
* greet
   - utter_greet
* ask_price[company=FB]
   - slot{"company": "FB"}
   - action_price
* thanks
   - utter_goodbye

## story_008
* greet
   - utter_greet
* ask_historical_plot[company=WMT, start_time=2018.2.1, end_time=2018.5.2]
   - slot{"company": "WMT"}
   - slot{"start_time": "2018.2.1"}
   - slot{"end_time": "2018.5.2"}
   - action_historical_plot
* goodbye
   - utter_goodbye

## story_009
* greet
   - utter_greet
* ask_historical_plot[company=AAPL, start_time=2018.5.3, end_time=2018.7.9]
   - slot{"company": "AAPL"}
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

