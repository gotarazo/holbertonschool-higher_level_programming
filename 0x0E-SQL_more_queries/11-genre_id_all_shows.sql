-- Lists all shows contained in the database hbtn_0d_tvshows
SELECT t.title, v.genre_id
  FROM tv_shows AS t LEFT JOIN tv_show_genres AS v ON t.id = v.show_id
 ORDER BY t.title, v.genre_id;
