build:
  artifacts:
    - image: pythonFile
deploy:
  kubectl:
    manifests:
      - k8s/web.yaml
      - k8s/backend.yaml
