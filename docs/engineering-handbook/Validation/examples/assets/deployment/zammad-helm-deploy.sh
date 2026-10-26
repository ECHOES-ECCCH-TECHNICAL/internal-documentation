helm upgrade --install zammad zammad/zammad \
  --version "${CHART_VERSION}" \
  -n "${NAMESPACE}" \
  -f "environments/${ENVIRONMENT}/values.yaml" \
  -f "environments/${ENVIRONMENT}/values-openshift.yaml" \
  -f "environments/${ENVIRONMENT}/values-images.yaml" \
  --atomic --wait --timeout "${HELM_TIMEOUT}"
