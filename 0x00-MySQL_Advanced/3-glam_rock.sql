-- lists all bands with Glam rock as their main style,
-- ranked by their longevitySELECT band_name, (IFNULL(split 2022) - formed) AS lifespan
SELECT band_name, (IFNULL(split, 2022) - formed) AS lifespan
FROM metal_bands WHERE style LIKE '%Glam rock%'
ORDER BY(lifespan) DESC;
