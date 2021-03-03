-- Lists all genres from hbtn_0d_tv shows along with number of shows linked to each
SELECT v.name AS genre, COUNT(*) AS number_of_shows
  FROM tv_genres AS v INNER JOIN tv_show_genres AS t ON v.id=t.genre_id
 GROUP BY v.name  ORDER BY number_of_shows DESC;
