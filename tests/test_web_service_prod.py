# -*- coding: utf-8 -*-
"""
Created on Wed May 30 12:05:46 2018

@author: MichaelEK
"""
import pytest
import pandas as pd
from hilltoppy.web_service import measurement_list, site_list, get_data, wq_sample_parameter_list

### Parameters
base_url = 'http://wateruse.ecan.govt.nz'

hts_names = ['AquiferManualQcEcanDaily', 'AquiferRecorderQcEcanDaily', 'AbstractionRawDaily', 'RiverManualQcEcanDaily', 'RiverRecorderQcEcanDaily', 'AtmosRecorderQcEcanDaily', 'RiverRecorderRawEcanDaily', 'AtmosRecorderRawEcanDaily', 'AquiferRecorderRawEcanDaily', 'WQAll']

### Tests

@pytest.mark.parametrize('hts', [h + '.hts' for h in hts_names])
def test_site_mtypes(hts):
    sites = site_list(base_url, hts)
    site1 = sites.iloc[2].SiteName
    mtype_df1 = measurement_list(base_url, hts, site1).reset_index().iloc[0]
    tsdata1 = get_data(base_url, hts, site1, mtype_df1.Measurement, from_date=str(mtype_df1.From), to_date=str(mtype_df1.From))
    assert len(tsdata1) == 1

