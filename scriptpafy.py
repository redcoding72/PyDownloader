import pafy
import humanize
video_link = "https://www.youtube.com/watch?v=57qFjCwvKsQ&t=2s"
v = pafy.new(video_link)
# print(v.title)
# print(v.duration)
# print(v.rating)
# print(v.author)
# print(v.length)
# print(v.keywords)
# print(v.thumb)
# print(v.videoid)
# print(v.viewcount)
# st = v.allstreams

# for s in st:
#     size = humanize.naturalsize(s.get_filesize())
#     print(s.mediatype, s.extension, s.quality, size)
