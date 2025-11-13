import streamlit as st
import pandas as pd
import numpy as np

# --- Page Configuration ---
st.set_page_config(
    page_title="Wavess 1.0 & 2.0 Prototype Showcase",
    page_icon="🌊",
    layout="wide"
)

# --- Helper Functions to Load Data ---
@st.cache_data
def load_data(post_file, audience_file):
    """Loads and caches the CSV data for Task 1."""
    try:
        post_df = pd.read_csv(post_file)
    except FileNotFoundError:
        post_df = None
    try:
        audience_df = pd.read_csv(audience_file)
    except FileNotFoundError:
        audience_df = None
    return post_df, audience_df

@st.cache_data
def load_markdown(md_file):
    """Loads and caches the Markdown report for Task 2."""
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return None

# --- Main App ---
st.title("🌊 Wavess 1.0 & 2.0 Prototype Showcase")
st.write("This dashboard presents the findings from the two technical tasks.")

# --- Load all data sources ---
post_df, audience_df = load_data('post_analysis_summary.csv', 'audience_icp_ranking.csv')
gtm_report_md = load_markdown('gtm_intelligence_report_stripe.md')

# --- Create Tabs for Each Task ---
tab1, tab2 = st.tabs(["Task 1: LinkedIn Post Analysis", "Task 2: GTM Intelligence Report"])

# ==============================================================================
# --- TAB 1: LinkedIn Post Analysis ---
# ==============================================================================
with tab1:
    st.header("Analysis of a Klarna LinkedIn Post")

    if post_df is not None:
        st.subheader("Post Performance Summary")
        
        # Display key metrics in a visually appealing way
        col1, col2, col3, col4 = st.columns(4)
        post_data = post_df.iloc[0]
        col1.metric("Sentiment", post_data['sentiment'])
        col2.metric("Total Engagement", f"{int(post_data['engagement_sum'])}")
        col3.metric("Likes", f"{int(post_data['likes_count'])}")
        col4.metric("Comments", f"{int(post_data['comments_count'])}")

        # Show the original post text in an expander
        with st.expander("View Original Post Text"):
            st.write(post_data['post_text'])
    else:
        st.error("`post_analysis_summary.csv` not found. Please ensure it's in the same directory.")

    st.markdown("---")

    if audience_df is not None:
        st.subheader("Audience Relevance & Composition")
        
        # Filter for individuals only for the summary
        individuals_df = audience_df[audience_df['is_individual'] == 1].copy()
        
        # Re-calculate summaries from the dataframe for display
        all_keywords = individuals_df[individuals_df['matched_keywords'].notna()]['matched_keywords'].apply(eval).explode()
        role_keys = {'sustainability', 'climate', 'esg', 'ai', 'data scientist', 'engineer', 'investor', 'venture', 'founder', 'entrepreneur', 'innovation', 'tech', 'consultant'}
        seniority_keys = {'ceo', 'chief', 'c-level', 'head of', 'vp', 'director', 'partner', 'lead', 'manager', 'senior', 'founder'}

        top_roles = all_keywords[all_keywords.isin(role_keys)].value_counts()
        top_seniority = all_keywords[all_keywords.isin(seniority_keys)].value_counts()
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Top Roles in Audience**")
            st.dataframe(top_roles.head(7).to_frame(name='Count'))
        with col2:
            st.write("**Top Seniority in Audience**")
            st.dataframe(top_seniority.head(7).to_frame(name='Count'))

        st.markdown("---")
        
        # Interactive table of the ranked audience
        st.subheader("Ranked Audience Explorer")
        min_score = int(individuals_df['relevance_score'].min())
        max_score = int(individuals_df['relevance_score'].max())
        
        score_threshold = st.slider(
            'Filter audience by minimum relevance score:',
            min_value=min_score,
            max_value=max_score,
            value=min_score,
            help="Show individuals with a relevance score greater than or equal to this value."
        )
        
        filtered_audience = individuals_df[individuals_df['relevance_score'] >= score_threshold]
        
        st.write(f"Displaying {len(filtered_audience)} of {len(individuals_df)} individuals.")
        
        st.dataframe(filtered_audience[[
            'name', 'headline', 'relevance_score', 'matched_keywords', 'reacted', 'commented', 'reshared'
        ]], use_container_width=True)

    else:
        st.error("`audience_icp_ranking.csv` not found. Please ensure it's in the same directory.")

# ==============================================================================
# --- TAB 2: GTM Intelligence Report ---
# ==============================================================================
with tab2:
    st.header("GTM Intelligence Report for Stripe")
    
    if gtm_report_md:
        st.markdown(gtm_report_md, unsafe_allow_html=True)
    else:
        st.error("`gtm_intelligence_report_stripe.md` not found. Please ensure it's in the same directory.")