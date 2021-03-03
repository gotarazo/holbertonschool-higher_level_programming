-- Lists all shows in the database hbtn_0d_tvshows without a genre linked
SELECT t.title, v.genre_id
  FROM tv_shows AS t LEFT JOIN tv_show_genres AS v ON t.id = v.show_id WHERE v.genre_id IS NULL
 ORDER BY t.title, v.genre_id;
