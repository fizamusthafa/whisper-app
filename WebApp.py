import streamlit as st
import pickle

# Load preprocessed data and similarity matrix
newdf = pickle.load(open('artifacts/mooc_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

# Function to recommend similar courses
def recommend(mooc_title):
    index = newdf[newdf['title'].str.lower() == mooc_title.lower()].index[0]
    distances = sorted(enumerate(similarity[index]), reverse=True, key=lambda x: x[1])
    similar_courses = [newdf.iloc[i[0]] for i in distances[1:8]]
    return similar_courses

# Read the contents of the CSS file
with open('design.css', 'r') as css_file:
    css_code = css_file.read()

# Streamlit UI
st.title('Open Online Course Recommender')

mooc_list = newdf['title'].tolist()
selected_mooc = st.selectbox('Type or select a course to get a recommendation', mooc_list)

if st.button('Recommend'):
    if selected_mooc:
        recommended_courses = recommend(selected_mooc)
        if recommended_courses:
            st.markdown(f'<style>{css_code}</style>', unsafe_allow_html=True)
            for course in recommended_courses:
                st.markdown(
                    f'<div class="recommended-course">'
                    f'<h3 class="course-title">{course.title}</h3>'
                    f'<p class="course-info"><strong>Subject:</strong> {course.displayed_subject}</p>'
                    f'<p class="course-info"><strong>Summary:</strong> {course.displayed_summary}</p>'
                    f'</div>',
                    unsafe_allow_html=True
                )
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.write('No recommendations found for the selected course.')
    else:
        st.write('Please select a course.')


# Additional Streamlit configurations
st.sidebar.title('About')
st.sidebar.info('This web app recommends similar MOOC courses based on course tags.')
