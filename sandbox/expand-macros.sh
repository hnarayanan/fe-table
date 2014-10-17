#!/bin/bash
sed \
-e 's/\\mP/\\mathcal{P}/g' \
-e 's/\\mQ/\\mathcal{Q}/g' \
-e 's/\\mS/\\mathcal{S}/g' \
-e 's/\\Pm{\([0-9]*\)}{\([0-9]*\)}{\([0-9]*\)}/\\mathcal{P}^-_{\1}\\Lambda^{\2}(\\Delta_{\3})/g' \
-e 's/\\P{\([0-9]*\)}{\([0-9]*\)}{\([0-9]*\)}/\\mathcal{P}_{\1}\\Lambda^{\2}(\\Delta_{\3})/g' \
-e 's/\\Qm{\([0-9]*\)}{\([0-9]*\)}{\([0-9]*\)}/\\mathcal{Q}^-_{\1}\\Lambda^{\2}(\\square_{\3})/g' \
-e 's/\\S{\([0-9]*\)}{\([0-9]*\)}{\([0-9]*\)}/\\mathcal{S}_{\1}\\Lambda^{\2}(\\square_{\3})/g' \
-e 's/\\pl/\\,+\\,/g' \
-e 's/\\dof{\([0-9]*\)}{\([0-9]*\)}{\([0-9]*\)}{\([0-9]*\)}{\([0-9]*\)}/\1\\times\\underbrace{\\mathcal{P}_{\2}\\Lambda^{\3}(\\Delta_{\4})}_{\5}/g' \
-e 's/\\dofm{\([0-9]*\)}{\([0-9]*\)}{\([0-9]*\)}{\([0-9]*\)}{\([0-9]*\)}/\1\\times\\underbrace{\\mathcal{P}^-_{\2}\\Lambda^{\3}(\\Delta_{\4})}_{\5}/g' \
-e 's/\\dofq{\([0-9]*\)}{\([0-9]*\)}{\([0-9]*\)}{\([0-9]*\)}{\([0-9]*\)}/\1\\times\\underbrace{\\mathcal{Q}^-_{\2}\\Lambda^{\3}(\\square_{\4})}_{\5}/g' \
-e 's/\\dofs{\([0-9]*\)}{\([0-9]*\)}{\([0-9]*\)}{\([0-9]*\)}{\([0-9]*\)}/\1\\times\\underbrace{\\mathcal{P}_{\2}\\Lambda^{\3}(\\square_{\4})}_{\5}/g'