import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    # print(data)
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w200/" + poster_path
    return full_path

def m_movie_overview(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    # print(data)
    return data['overview'], data['runtime'],data['revenue'], data['release_date'],data['tagline']
    
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    movie_overview = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

        overview,runtime,revenue,release_date,tagline = m_movie_overview(movie_id)
        # overview = overview.split('.')[0]
        movie_overview.append([overview,runtime,revenue,release_date,tagline])

    return recommended_movie_names,recommended_movie_posters,movie_overview,

st.header('Movie Recommender System')
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters,movie_overview = recommend(selected_movie)
    tab1, tab2, tab3,tab4,tab5 = st.tabs(recommended_movie_names)

    with tab1:
        col1,col2,col3 = st.columns(3)
        col1.image(recommended_movie_posters[0],width=250)
        st.write("\n\n")
        col2.success("Runtime : "+ str(movie_overview[0][1])+ " min")
        col2.success("Revenue : "+ str(movie_overview[0][2]))
        col2.success ("Release Date  : " + movie_overview[0][3] )
        col2.success ("Movie Name  : "+recommended_movie_names[0])

        col3.success(movie_overview[0][0])
        col2.success("Movie TagLine  : "+movie_overview[0][4])

    with tab2:
        col1,col2,col3 = st.columns(3)
        col1.image(recommended_movie_posters[1],width=250)
        col3.success(movie_overview[1][0])

        col2.success("Runtime  : "+ str(movie_overview[1][1])+ " min")
        col2.success("Revenue  : "+ str(movie_overview[1][2]))
        col2.success ("Release Date   : " + movie_overview[1][3] )
        col2.success ("Movie Name   : "+recommended_movie_names[1])
        col2.success("Movie TagLine  : "+movie_overview[1][4])


    with tab3:
        col1,col2,col3 = st.columns(3)
        col1.image(recommended_movie_posters[2],width=250)

        col3.success(movie_overview[2][0])
        

        col2.success("Runtime  : "+ str(movie_overview[2][1])+ " min")
        col2.success("Revenue  : "+ str(movie_overview[2][2]))
        col2.success ("Release Date   : " + movie_overview[2][3] )
        col2.success ("Movie Name   : "+recommended_movie_names[2])
        col2.success("Movie TagLine  : "+ movie_overview[2][4])

    with tab4:
        col1,col2,col3 = st.columns(3)
        col1.image(recommended_movie_posters[3],width=250)

        col3.success(movie_overview[3][0])
        
        col2.success("Runtime  : "+ str(movie_overview[3][1])+ " min")
        col2.success("Revenue  : "+ str(movie_overview[3][2]))
        col2.success ("Release Date   : " + movie_overview[3][3] )
        col2.success ("Movie Name   : "+recommended_movie_names[3])
        col2.success("Movie TagLine  : "+ movie_overview[3][4])


    with tab5:
        col1,col2,col3 = st.columns(3)
        col1.image(recommended_movie_posters[4],width=250)

        col3.success(movie_overview[4][0])
        
        col2.success("Runtime  : "+ str(movie_overview[4][1])+ " min")
        col2.success("Revenue  : "+ str(movie_overview[4][2]))
        col2.success ("Release Date   : " + movie_overview[4][3] )
        col2.success ("Movie Name  : "+recommended_movie_names[4])
        col2.success("Movie TagLine  : "+movie_overview[4][4])




