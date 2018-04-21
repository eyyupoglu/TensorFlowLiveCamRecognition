import github3


gh = github3.login(username='eyyupoglu', password ='mamet0012')
repository = gh.repository('', 'TensorFlowLiveCamRecognition')

fileName = "mehmet.jpg"
with open(fileName, 'rb') as fd:
    contents = fd.read()
    repository.create_file(
        path=fileName,
        message='Start tracking {!r}'.format(fileName),
        content=contents,
    )