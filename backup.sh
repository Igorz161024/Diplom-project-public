#!/bin/bash
while true; do
  pg_dump -h db -U postgres -d erp_diplom > /backups/erp_diplom_$(date +%F_%H-%M).sql
  sleep 86400
done
