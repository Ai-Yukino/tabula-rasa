# Randomly sample 12 records using RSQLite
# https://rsqlite.r-dbi.org/articles/rsqlite
# *****************************************************************************

## Import R packages
###############################################################################

library(tidyverse)
library(DBI)

## Set working directory for R Studio
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

wd <- getwd() %>% str_replace("/02$", "")
setwd(wd)
getwd()
rm(wd)

## Load database
###############################################################################

db <- dbConnect(RSQLite::SQLite(), "data/02/02_before_solutions.db")

## Get max(id) of tables
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

max_id_songs <- as.integer(dbGetQuery(db, "SELECT max(id) FROM songs"))
max_id_genres <- as.integer(dbGetQuery(db, "SELECT max(id) FROM genres"))
max_id_artists <- as.integer(dbGetQuery(db, "SELECT max(id) FROM artists"))
max_id_albums <- as.integer(dbGetQuery(db, "SELECT max(id) FROM albums"))
max_id_favorite <- as.integer(dbGetQuery(db, "SELECT max(FavoriteID) 
                                         FROM favorite"))

## Randomly sample 12 songs from the songs table
###############################################################################

seed <- -06022022

set.seed(seed)
sample_ids_songs <- sample(1:max_id_songs, 12)

query <- dbGetQuery(db, "SELECT songs.id AS songs_id, albums.id AS albums_id,
           albums.genre_id, albums.artist_id
           FROM songs
           INNER JOIN albums ON songs.album_id = albums.id
           WHERE songs.id = ?",
           params = list(sample_ids_songs))

## Randomly sample 12 rows from the favorite table
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sample_ids_favorite <- sample(1:max_id_favorite, 12)

df <- query %>%
  mutate(FavoriteID = sample_ids_favorite) %>%
  select(FavoriteID, everything())

## Export result as a csv file
###############################################################################

file_name <- paste0("./data/02/sample_songs_", seed, ".csv")

write_csv(df, file_name)
