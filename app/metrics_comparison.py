import streamlit as st
import plotly.express as px

# Metrics Functions

def calculate_max_hp(cleaned_df):
    """Calculate the highest HP across the set"""
    return cleaned_df["hp"].max()

def calculate_max_attack(cleaned_df):
    """Calculate the highest attack across the set"""
    return cleaned_df["attack"].max()

def calculate_max_defense(cleaned_df):
    """Calculate the highest defense across the set"""
    return cleaned_df["defense"].max()

def calculate_max_sp_attack(cleaned_df):
    """Calculate the highest special attack across the set"""
    return cleaned_df["sp_attack"].max()

def calculate_max_sp_defense(cleaned_df):
    """Calculate the highest special defense across the set"""
    return cleaned_df["sp_defense"].max()

def calculate_max_speed(cleaned_df):
    """Calculate the highest special speed across the set"""
    return cleaned_df["speed"].max()


# Pick additional random Pokemon

random_pokemon = df.sample(5)

# Calculate metrics

selected_pokemon = 

# Visualisation functions

def calculate_percentage_xp(cleaned_df, name):
    """Calculate the percentage of selected Pokemon's XP against the highest across the set"""
    percentage_xp = name.hp / max_hp
    
# Comparison chart

