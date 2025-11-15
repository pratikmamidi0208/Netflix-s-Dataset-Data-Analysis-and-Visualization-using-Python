import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('netflix_titles.csv')
df.drop(columns=['description'], inplace=True)

df = df.dropna(subset=['type', 'release_year', 'rating', 'country', 'duration'])

type_counts = df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index, type_counts.values, color=['blue', 'red'])
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('Movies_VS_TVShows.png')

ratings_counts = df['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(ratings_counts, labels=ratings_counts.index, startangle=90)
plt.title('Percentage of Content ratings')
plt.tight_layout()
plt.savefig('content_ratings_pie.png')


movie_df = df[df['type'] == 'Movie'].copy()
movie_df['duration_int'] = movie_df['duration'].str.replace('min', '').astype(int)

plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'], bins=30, color = 'purple', edgecolor= 'black')
plt.title('Distribution of Movie Duration')
plt.xlabel('DURATION (minutes)')
plt.ylabel('No of Movies')
plt.tight_layout()
plt.savefig('movieduraiton_distribution.png')

release_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_counts.index, release_counts.values, marker="o", color="red", label='Releases in a year')
plt.xlabel('Years')
plt.ylabel('No of shows')
plt.grid(True)
plt.savefig('releasecounts_scatplot.png')


country_counts = df['country'].value_counts().head(20)
plt.figure(figsize=(8,6))
plt.barh(country_counts.index, country_counts.values, color = 'Teal')
plt.title('Top 20 countries by the number of shows')
plt.xlabel('Number of Shows')
plt.ylabel('Country')
plt.grid(True)
plt.savefig('top20countries_by_shows.png')
plt.show()

content_by_year = df.groupby(['release_year', 'type']).size().unstack().fillna(0)
fig, ax = plt.subplots(1,2, figsize = (12,5))

#first subplot: movies
ax[0]. plot(content_by_year.index, content_by_year['Movie'], color = 'blue')
ax[0].set_title('Movies released per year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')

#second subplot:TV Shows
ax[1].plot(content_by_year.index, content_by_year['TV Show'], color='orange')
ax[1].set_title('TV shows released per year')
ax[1].set_xlabel('Year')
ax[1].set_ylabel('Number of Shows')

fig.suptitle('comparison of Movies and TV shows released over years')
plt.tight_layout()
plt.savefig('MnT_comparision.png')
plt.show()
