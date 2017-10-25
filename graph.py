import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sodapy import Socrata

def display_graph():
  #Initializing clients for Chicago, NYC, and Boston
  chiclient = Socrata("data.cityofchicago.org",None)
  #nycclient = Socrata("data.cityofnewyork.us",None)
  bosclient = Socrata("data.cityofboston.gov",None)

  #Code for Chicago Crime
  chi_thefts=chiclient.get("6zsd-86xi",year=2015,community_area=72,primary_type='THEFT')
  chi_assaults=chiclient.get("6zsd-86xi",year=2015,community_area=72,primary_type='ASSAULT')

  chi_thefts_df=pd.DataFrame.from_records(chi_thefts)
  chi_assaults_df=pd.DataFrame.from_records(chi_assaults)

  chi_theft_y=chi_thefts_df["primary_type"].count()
  chi_assault_y=chi_assaults_df["primary_type"].count()

  chi_frequency=[chi_theft_y,chi_assault_y]

  #Code for NYC Crime
  ##nyc_thefts=nycclient.get("qgea-i56i",rpt_dt="2015-12-31",addr_pct_cd=10,ofns_desc='ROBBERY')
  ##nyc_assaults=nycclient.get("qgea-i56i",rpt_dt="2015-12-31",addr_pct_cd=10,ofns_desc='ASSAULT 3')
  ##
  ##nyc_thefts_df=pd.DataFrame.from_records(nyc_thefts)
  ##nyc_assaults_df=pd.DataFrame.from_records(nyc_assaults)

  #nyc_theft_y=nyc_thefts_df["ofns_desc"].count()
  #nyc_assault_y=nyc_assaults_df["ofns_desc"].count()

  #nyc_frequency=[nyc_theft_y,nyc_assault_y]

  #Code for Boston Crime
  bos_thefts=bosclient.get("ufcx-3fdn",year=2015,reptdistrict="A1",incident_type_description='ROBBERY')
  bos_assaults=bosclient.get("ufcx-3fdn",year=2015,reptdistrict="A1",incident_type_description='SIMPLE ASSAULT')

  bos_thefts_df=pd.DataFrame.from_records(bos_thefts)
  bos_assaults_df=pd.DataFrame.from_records(bos_assaults)

  bos_theft_y=bos_thefts_df["incident_type_description"].count()
  bos_assault_y=bos_assaults_df["incident_type_description"].count()

  bos_frequency=[bos_theft_y,bos_assault_y]

  n=2
  fig, ax = plt.subplots()
  ind = np.arange(n)
  width=0.35

  chidata=ax.bar(ind,chi_frequency,width,color='blue',label='Chicago')
  bosdata=ax.bar(ind+width,bos_frequency,width,color='cyan',label='Boston')

  #Independent Variables
  ax.set_xticks(ind + width / 2)
  ax.set_xticklabels(('Theft','Assault'))

  #Plotting each
  plt.xlabel('Crimes')
  plt.ylabel('Number of Occurrences')
  plt.title('Crimes in Your Selected Area')
  plt.legend()
  plt.tight_layout()
  image=plt.savefig('graph.png')
  return(image)
