
# coding: utf-8

# In[13]:


# Dependencies and Setup
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Hide warning messages in notebook
import warnings
warnings.filterwarnings('ignore')

# File to Load (Remember to Change These)
mouse_drug_data_to_load = "data/mouse_drug_data.csv"
clinical_trial_data_to_load = "data/clinicaltrial_data.csv"

# Read the Mouse and Drug Data and the Clinical Trial Data
mouse_df = pd.read_csv(mouse_drug_data_to_load)
clin_df = pd.read_csv(clinical_trial_data_to_load)

# Combine the data into a single dataset
combined_df = pd.merge(mouse_df,clin_df, on =['Mouse ID','Mouse ID'])
# Display the data table for preview
combined_df.head()


# ## Tumor Response to Treatment

# In[14]:


# Store the Mean Tumor Volume Data Grouped by Drug and Timepoint 
drug_mean = combined_df.groupby(["Drug", "Timepoint"]).mean()["Tumor Volume (mm3)"]
# Convert to DataFrame
drug_mean = pd.DataFrame(drug_mean)
# Preview DataFrame
drug_mean.head()


# In[15]:


# Set column to measure 
column = "Tumor Volume (mm3)"

# Great a grouping dataframe to visualize average tumor growth over the course of the timepoints
drug_grouping = combined_df.groupby(["Drug", "Timepoint"])

# List the average Tumor Volume for our grouping in a dataframe
df_avg_vol = pd.DataFrame(drug_grouping[column].mean()).reset_index()
df_avg_vol.head(10)


# In[16]:


# Store the Standard Error of Tumor Volumes Grouped by Drug and Timepoint
drug_sem = combined_df.groupby(["Drug", "Timepoint"]).sem()["Tumor Volume (mm3)"]
# Convert to DataFrame
drug_sem = pd.DataFrame(drug_sem)
# Preview DataFrame
drug_sem.head() 


# In[17]:


#same as box 2################################################################
column = "Tumor Volume (mm3)"

# Great a grouping dataframe to visualize average tumor growth over the course of the timepoints
drug_grouping = combined_df.groupby(["Drug", "Timepoint"])

# List the average Tumor Volume for our grouping in a dataframe
df_avg_vol_sems = pd.DataFrame(drug_grouping[column].std()).reset_index()
df_avg_vol_sems.head(10)


# In[18]:


# Minor Data Munging to Re-Format the Data Frames
drug_mean = drug_mean.reset_index()
df_table_mean = drug_mean.pivot(index="Timepoint", columns="Drug")["Tumor Volume (mm3)"]
# Create drug summary table for Tumor Volume
drug_sem = drug_sem.reset_index()
df_table_sems = drug_sem.pivot(index="Timepoint", columns="Drug")["Tumor Volume (mm3)"]
# Preview that Reformatting worked
df_table_mean.head()


# In[19]:


df_table_sems.head()


# In[33]:


# Generate the Plot (with Error Bars)
plt.figure(figsize=(8,5))
plt.errorbar(df_table_mean.index, df_table_mean["Capomulin"], yerr=df_table_sems["Capomulin"],marker='o',color='r',markersize=5,linestyle='dashed',linewidth=0.5,capsize=5) 
plt.errorbar(df_table_mean.index, df_table_mean["Infubinol"], yerr=df_table_sems["Infubinol"],marker='^',color='y',markersize=5,linestyle='dashed',linewidth=0.5,capsize=5)
plt.errorbar(df_table_mean.index, df_table_mean["Ketapril"], yerr=df_table_sems["Ketapril"],marker='*',color='g',markersize=5,linestyle='dashed',linewidth=0.5,capsize=5)
plt.errorbar(df_table_mean.index, df_table_mean["Placebo"], yerr=df_table_sems["Placebo"],marker='+',color='b',markersize=5,linestyle='dashed',linewidth=0.5,capsize=5)           
             

plt.ylim(20, 80)
plt.xlim(0, 45)

             
plt.title("Tumor Response to Treatment", fontsize=20)
plt.xlabel("Time (Days)", fontsize=15)
plt.ylabel("Tumor Volume (mm3)", fontsize=15)
plt.grid(linestyle = 'dashed')
plt.legend(loc= "best", fontsize="small",fancybox=True)
plt.savefig('Fig1.png')
# Call function to create scatter plots for Tumor Volume data
plt.show()
# Display scatter plot
# Save the Figure


# In[34]:


# Show the Figure
plt.show()


# ## Metastatic Response to Treatment

# In[22]:


# Store the Mean Met. Site Data Grouped by Drug and Timepoint 
meta_df = combined_df.groupby(["Drug","Timepoint"]).mean()["Metastatic Sites"]
# Convert to DataFrame
meta_df = pd.DataFrame(meta_df)
# Preview DataFrame
meta_df.head()


# In[6]:





# In[25]:


# Store the Standard Error associated with Met. Sites Grouped by Drug and Timepoint 
meta_df_sem = combined_df.groupby(["Drug", "Timepoint"]).sem()["Metastatic Sites"]
# Convert to DataFrame
meta_df_sem = pd.DataFrame(meta_df_sem)
# Preview DataFrame
meta_df_sem.head()


# In[28]:


# Minor Data Munging to Re-Format the Data Frames
meta_df = meta_df.reset_index()
meta_sites_pivotm = meta_df.pivot(index="Timepoint", columns="Drug")["Metastatic Sites"]
# Preview that Reformatting worked
meta_df_sem = meta_df_sem.reset_index()
meta_sites_pivots = meta_df_sem.pivot(index="Timepoint", columns="Drug")["Metastatic Sites"]

meta_sites_pivotm.head()


# In[29]:


meta_sites_pivots.head()


# In[36]:


# Generate the Plot (with Error Bars)

plt.figure(figsize=(8,5))
plt.errorbar(meta_sites_pivotm.index, meta_sites_pivotm["Capomulin"], yerr=meta_sites_pivots["Capomulin"],marker='o',color='r',markersize=5,linestyle='dashed',linewidth=0.5,capsize=5) 
plt.errorbar(meta_sites_pivotm.index, meta_sites_pivotm["Infubinol"], yerr=meta_sites_pivots["Infubinol"],marker='^',color='y',markersize=5,linestyle='dashed',linewidth=0.5,capsize=5)
plt.errorbar(meta_sites_pivotm.index, meta_sites_pivotm["Ketapril"], yerr=meta_sites_pivots["Ketapril"],marker='*',color='g',markersize=5,linestyle='dashed',linewidth=0.5,capsize=5)
plt.errorbar(meta_sites_pivotm.index, meta_sites_pivotm["Placebo"], yerr=meta_sites_pivots["Placebo"],marker='+',color='b',markersize=5,linestyle='dashed',linewidth=0.5,capsize=5)           
             

plt.ylim(0, 4)
plt.xlim(0, 45)

             
plt.title("Metastatic Treatment", fontsize=20)
plt.xlabel("Duration (Days)", fontsize=15)
plt.ylabel("Metastatic Sites", fontsize=15)
plt.grid(linestyle = 'dashed')
plt.legend(loc= "best", fontsize="small",fancybox=True)
plt.savefig('Fig2.png')
# Call function to create scatter plots for Tumor Volume data
plt.show()





# Save the Figure

# Show the Figure


# In[9]:





# ## Survival Rates

# In[38]:


# Store the Count of Mice Grouped by Drug and Timepoint (W can pass any metric)
mouse_df = combined_df.groupby(["Drug","Timepoint"]).count()["Tumor Volume (mm3)"]
# Convert to DataFrame
mouse_df = pd.DataFrame({"Mouse Count": mouse_df})
# Preview DataFrame
mouse_df.head()


# In[10]:





# In[39]:


# Minor Data Munging to Re-Format the Data Frames
mouse_df = mouse_df.reset_index()
mouse_df_rf = mouse_df.pivot(index="Timepoint", columns="Drug")["Mouse Count"] 
# Preview the Data Frame
mouse_df_rf.head()


# In[11]:





# In[40]:


# Generate the Plot (Accounting for percentages)
plt.figure(figsize=(8,5))
plt.plot(100 * mouse_df_rf["Capomulin"]/25,"ro", linestyle="dashed",markersize=5,linewidth=0.5) 
plt.plot(100 * mouse_df_rf["Infubinol"]/25,"b", linestyle="dashed",markersize=5,linewidth=0.5)  
plt.plot(100 * mouse_df_rf["Ketapril"]/25,"gs", linestyle="dashed",markersize=5,linewidth=0.5)
plt.plot(100 * mouse_df_rf["Placebo"]/25,"kd", linestyle="dashed",markersize=5,linewidth=0.5)


plt.ylim(30, 100)
plt.xlim(0, 45)

             
plt.title("Survival Rate", fontsize=20)
plt.xlabel("Time (Days)", fontsize=15)
plt.ylabel("Survival Rate (%)", fontsize=15)
plt.grid(linestyle = 'dashed')
plt.legend(loc= "best", fontsize="small",fancybox=True)
plt.savefig('Fig3.png')
# Save the Figure

# Show the Figure
plt.show()


# In[12]:





# ## Summary Bar Graph

# In[47]:


# Calculate the percent changes for each drug
percent_change = 100 * (df_table_mean.iloc[-1] - df_table_mean.iloc[0]) / df_table_mean.iloc[0]
# Display the data to confirm
percent_change


# In[13]:





# In[ ]:


# Store all Relevant Percent Changes into a Tuple
changes_pct = (percent_change["Capomulin"]
               percent_change["Infubinol"]
               percent_change["Ketapril"]
               percent_change["Placbo"]
              )

# Splice the data between passing and failing drugs
fig, ax = plt.subplots()
ind = np.arange(len(changes_pct))
width = 1

# Orient widths. Add labels, tick marks, etc. 


# Use functions to label the percentages of changes


# Call functions to implement the function calls


# Save the Figure


# Show the Figure
fig.show()


# In[14]:




