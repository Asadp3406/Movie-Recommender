import pickle
import streamlit as st
import requests
import time

@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=2171b9b5556bd2747edf8e75b027aafe&language=en-US"
    
    for attempt in range(3):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            poster_path = data.get('poster_path')
            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"
            return None
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
            if attempt < 2:
                time.sleep(2)
                continue
            return None
        except Exception as e:
            return None
    return None

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])
    
    recommended_movies = []
    recommended_posters = []
    
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        poster = fetch_poster(movie_id)
        recommended_posters.append(poster)
    
    return recommended_movies, recommended_posters

st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")

st.title("🎬 Movie Recommender System")
st.markdown("Discover movies similar to your favorites")

movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity_compressed.pkl', 'rb'))

selected_movie = st.selectbox("Select a movie", movies['title'].values)

if st.button('Get Recommendations', type="primary"):
    with st.spinner('Finding similar movies...'):
        try:
            names, posters = recommend(selected_movie)
            
            st.markdown("---")
            st.subheader("Recommended for you:")
            
            cols = st.columns(5)
            for idx, col in enumerate(cols):
                with col:
                    st.markdown(f"**{names[idx]}**")
                    if posters[idx]:
                        st.image(posters[idx], use_container_width=True)
                    else:
                        st.info("Poster not available")
        except Exception as e:
            st.error("An error occurred while fetching recommendations. Please try again.")
            st.exception(e)
