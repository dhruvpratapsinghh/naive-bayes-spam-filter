import streamlit as st

st.set_page_config(page_title="Spam Detector", page_icon="📧")

st.title("📧 Email Spam Analyzer")
st.write("Paste an email below to calculate its spam risk score based on suspicious keywords.")

# List of words used by spam Emails
spam_keywords = [
    "free", "you are selected", "click on the link", "urgent", "winner", "guaranteed", "no catch",
    "earn money", "cash prize", "credit card", "investment", "lottery", "act now", "claim your",
    "100% satisfied", "risk-free", "dear friend","limited time", "exclusive deal", "congratulations",
    "account suspended", "click here", "double your income", "wire transfer", "invoice attached", 
    "action required", "no hidden fees", "cancel at any time", "winner", "update your password", "security alert"
]

# Get the email from the user
email_text = st.text_area("Paste the email content here:", height=200)

#  Analysis Email
if st.button("Analyze Email"):
    if email_text.strip() == "":
        st.warning("Please paste an email first!")
    else:
        # Convert text to lowercase so "FREE" and "free" are treated the same
        email_lower = email_text.lower()
        
        # Scan the email for our trigger words
        found_words = []
        for word in spam_keywords:
            if word in email_lower:
                found_words.append(word)
        
        # 4. Calculate the Spam Score and Display Results
        st.subheader("Analysis Results")
        
        if len(found_words) == 0:
            st.success("✅ **Status: Safe** - No obvious spam keywords found.")
            st.progress(0)
            
        elif len(found_words) <= 2:
            st.warning("⚠️ **Status: Suspicious** - Proceed with caution.")
            st.write(f"**Trigger words found:** {', '.join(found_words)}")
            # Calculate a minor risk score (e.g., 2 words = 40%)
            spam_score = len(found_words) * 20
            st.progress(spam_score)
            
        else:
            st.error("🚨 **Status: High Spam Probability!**")
            st.write(f"**Trigger words found:** {', '.join(found_words)}")
            # Cap the score at 100%
            spam_score = min(len(found_words) * 25, 100)
            st.write(f"**Risk Score: {spam_score}%**")
            st.progress(spam_score)