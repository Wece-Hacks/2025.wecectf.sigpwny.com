import{m as o,c as n,C as e}from"./index.7e48942e.js";import{g as r}from"./userscore.a96f94fa.js";import{e as l}from"./index.b6afda34.js";import"./echarts.128204f2.js";window.Alpine=o;o.data("TeamGraphs",()=>({solves:null,fails:null,awards:null,solveCount:0,failCount:0,awardCount:0,getSolvePercentage(){return(this.solveCount/(this.solveCount+this.failCount)*100).toFixed(2)},getFailPercentage(){return(this.failCount/(this.solveCount+this.failCount)*100).toFixed(2)},getCategoryBreakdown(){const s=[],a={};this.solves.data.map(t=>{s.push(t.challenge.category)}),s.forEach(t=>{t in a?a[t]+=1:a[t]=1});const i=[];for(const t in a)i.push({name:t,count:a[t],percent:(a[t]/s.length*100).toFixed(2),color:n(t)});return i},async init(){this.solves=await e.pages.teams.teamSolves(window.TEAM.id),this.fails=await e.pages.teams.teamFails(window.TEAM.id),this.awards=await e.pages.teams.teamAwards(window.TEAM.id),this.solveCount=this.solves.meta.count,this.failCount=this.fails.meta.count,this.awardCount=this.awards.meta.count;let s=window.teamScoreGraphChartOptions;l(this.$refs.scoregraph,r(window.TEAM.id,window.TEAM.name,this.solves.data,this.awards.data,s))}}));o.start();
