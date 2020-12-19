#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 22:21:30 2020

@author: iman
"""
def search_jobs(driver, job_title_input, location_input):
    """Enter query terms into search box and run job search"""
    job_title = driver.find_element_by_xpath('.//input[@id="sc.keyword"]')
    job_title.send_keys(job_title_input)
    location = driver.find_element_by_xpath('.//input[@id="sc.location"]')
    location.clear()
    location.send_keys(location_input)
    driver.find_element_by_xpath('.//button[@type="submit"]').click()
    return